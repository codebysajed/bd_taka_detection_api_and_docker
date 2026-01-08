import os, uuid
import hashlib
import redis
import json
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import ValidationError
from app.model import model_load, object_detect
from app.schma import Imageinput, Prediction

app = FastAPI(title='Bangla Taka Detection model')

try:
    r = redis.Redis(host="redis", port=6379, db=0)
    r.ping()
    print('Redis connected and active')
except Exception as e:
    r = None
    print('Redis not connect:', str(e))


@app.get('/')
def home():
    return 'FastAPI is running'


@app.get('/health')
def health():
    return {
        'Status': 'ok',
        'model_loaded': model_load
    }


def hash_gen(file_bytes: bytes) -> str:
    return 'file:' + hashlib.md5(file_bytes).hexdigest()

@app.post('/predict', response_model=Prediction)
async def predict(file: UploadFile = File(...)):

    try:
        Imageinput(filename=file.filename)
    except ValidationError as e:
        errors = e.errors()[0]['msg']
        raise HTTPException(status_code=400, detail=errors)

    file_bytes = await file.read()
    cache_key = hash_gen(file_bytes)

    if r:
        cache_data = r.get(cache_key)
        if cache_data:
            print('Cache hit')
            return json.loads(cache_data)

    ext = file.filename.split(".")[-1].lower()
    image_path = f"temp_{uuid.uuid4()}.{ext}"
    with open(image_path, 'wb') as f:
        f.write(file_bytes)

    try:
        detections = object_detect(image_path)
        detections = [i.dict() for i in detections]
    except Exception as e:
        if os.path.exists(image_path):
            os.remove(image_path)
        raise HTTPException(status_code=500, detail=str(e))

    if os.path.exists(image_path):
        os.remove(image_path)

    if r:
        r.setex(cache_key, 60, json.dumps(detections))

    return Prediction(detection=detections)
