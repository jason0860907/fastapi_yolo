# FastAPI YOLO Object Detection

This application uses FastAPI framework and YOLO model for object detection.

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/jason0860907/fastapi_yolo
   ```

2. Navigate into the directory:

   ```bash
   cd fastapi_yolo
   ```

3. Install dependencies:

   ```bash
   pip install fastapi
   pip install ultralytics
   pip install io
   ```

4. Run the application:

   ```bash
   uvicorn fastapi_test:app --reload
   ```

5. (Option) Upload an image using HTTP POST request to the `/upload` route. Example:

   ```bash
   curl -X 'POST' \
     'http://localhost:8000/upload' \
     -F 'file=@/path/to/your/image.jpg'
   ```

6. (Option) Upload an image using Swagger UI

     - Open your web browser and go to http://localhost:8000/docs. This will open SwaggerUI, which provides a graphical interface for interacting with the API.

     - Click on the /upload endpoint to expand it.

     - Click on the "Try it out" -> "Choose File" -> "Execute" and see the detection results.

7. Detection Results
      - After uploading an image using the /upload endpoint, the application performs object detection using the YOLO ONNX model. The detected objects along with their bounding boxes are returned as a JSON object in the response.
      - Each detected object is represented by its class label and the coordinates of its bounding box (xmin, ymin, xmax, ymax).


## Notes

- Make sure to install the required Python libraries and YOLO model file `yolov8n.onnx`.
