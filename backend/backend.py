from flask import Flask, request
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/upload_video', methods=['POST'])
def upload_video():
    file = request.files['file']
    np_img = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    # Process the frame (e.g., display it)
    cv2.imshow("Webcam Stream", frame)
    cv2.waitKey(1)
    return "Frame received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Localhost setup
