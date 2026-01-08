from pydantic import BaseModel, validator


class Imageinput(BaseModel):
    filename: str


    @validator("filename")
    def image_validation(cls, file):
        allow_ext = ['png', 'jpg','jpeg']
        ext = file.split('.')[-1].lower()

        if ext not in allow_ext:
            raise ValueError( f"Invalid file type! Allowed: {allow_ext}")
        return file
    
class Bbox(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int

class Detection(BaseModel):
    clss: str
    conf: float
    bbox: Bbox

class Prediction(BaseModel):
    detection: list[Detection]