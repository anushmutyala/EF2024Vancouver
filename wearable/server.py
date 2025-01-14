# Flask Backend Script
from flask import Flask, request, send_file
from io import BytesIO
import threading

app = Flask(__name__)

# Variable to store the latest image data
latest_image = None
image_lock = threading.Lock()

@app.route('/upload', methods=['POST'])
def upload_image():
    global latest_image
    if 'image' not in request.files:
        return "No image provided", 400

    # Save the uploaded image data to the variable
    with image_lock:
        latest_image = BytesIO(request.files['image'].read())

    return "Image received", 200

@app.route('/display', methods=['GET'])
def display_image():
    global latest_image
    with image_lock:
        if latest_image is None:
            return "No image available", 404

        latest_image.seek(0)
        return send_file(latest_image, mimetype='image/jpeg')

@app.route('/', methods=['GET'])
def landing():
    return "hi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
