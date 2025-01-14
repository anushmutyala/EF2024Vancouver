import cv2
import time
import requests
from io import BytesIO

# Server URL (replace with your actual server address)
SERVER_URL = "http://127.0.0.1:5000/upload"

# Open the camera (camera index 0 typically refers to the Pi camera)
cap = cv2.VideoCapture(0)
#time.sleep(5)  # Wait 2 seconds for the camera to initialize

# Set resolution (adjust as needed)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

try:
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read a frame.")
            break

        # Encode the frame as a JPEG image
        _, encoded_image = cv2.imencode('.jpg', frame)

        # Send the image to the server
        response = requests.post(SERVER_URL, files={"image": BytesIO(encoded_image.tobytes())})

        if response.status_code == 200:
            print("Image successfully sent to the server.")
        else:
            print(f"Failed to send image: {response.status_code}")

        # Wait 5 seconds before capturing the next frame
        time.sleep(5)

except KeyboardInterrupt:
    print("Script stopped by user.")

finally:
    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

