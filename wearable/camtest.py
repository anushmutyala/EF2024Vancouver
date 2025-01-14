from picamzero import Camera
import base64
from time import sleep

cam = Camera()
cam.start_preview()
cam.pc2.capture_file("image.jpg")
with open("image.jpg", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
print(encoded_image)
sleep(5)