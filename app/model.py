import os
from ultralytics import YOLO

from app.schma import Detection, Bbox

model_path = os.path.join('model', 'best.pt')

model = YOLO(model_path)
model_load = True if model else False

class_names = model.names

def object_detect(img_path):

    result = model(img_path)

    detection = []

    for i in result:
        for box in i.boxes:
            cls_id = int(box.cls[0])
            name = class_names[cls_id]
            x1,y1,x2,y2  = map(int,box.xyxy[0].tolist())
            confidense = float(box.conf[0])
            detection.append(Detection(clss=name,conf=round(confidense,2),bbox=Bbox(x1=x1,y1=y1,x2=x2,y2=y2)))   

           
    return detection

# image_path = os.path.join('images', '100_191.jpg')
# print(object_detect(image_path))