from fastapi import FastAPI, UploadFile
from ultralytics import YOLO
from PIL import Image
import io


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.post("/upload")
async def upload_file(file: UploadFile):
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    output_cls_box = detect(img)
    return {"filename": file.filename, 'output_cls_box': output_cls_box}

def detect(img):
    model = YOLO("yolov8n.onnx")
    results = model(img)
    output_cls_box = []
    for i, r in enumerate(results):
        detected_cls = r.boxes.cls.cpu().tolist()
        detected_box = r.boxes.xyxy.cpu().tolist()
        for i, (temp_cls, temp_box) in enumerate(zip(detected_cls, detected_box)):
            # print(r.names[int(temp_cls)], temp_box)
            output_cls_box.append({"index": i, 
                                    "class": r.names[int(temp_cls)], 
                                    "x1": temp_box[0], 
                                    "y1": temp_box[1], 
                                    "x2": temp_box[2], 
                                    "y2": temp_box[3]})
    return output_cls_box