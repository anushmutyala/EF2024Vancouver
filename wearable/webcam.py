import cv2
import requests
import time

# Set the server URL to point to the local server
SERVER_URL = "http://192.168.1.10:5000/upload_video"  # No need to change anything else

camera = cv2.VideoCapture(1)
print("got capture")

while True:
    success, frame = camera.read()
    if not success:
        print("was not successful")
        break
    print("got camera")

    # Encode frame to JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    frame_data = buffer.tobytes()
    
    # Send frame to server
    print("req sent")
    print(frame_data)
    response = requests.post(SERVER_URL, files={"file": ("frame.jpg", frame_data, "image/jpeg")})
    print("after req")
    if response.status_code != 200:
        print("Failed to send frame:", response.text)

    time.sleep(5)


