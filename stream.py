from flask import Flask, Response
from ultralytics import YOLO
import cv2

app = Flask(__name__)
model = YOLO("hat_model.pt")

def generate_frames():
    for result in model.predict(source="http://192.168.100.11:8080/video", stream=True, conf=0.35):
        frame = result.plot()
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/stream')
def stream():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
