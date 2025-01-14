from flask import Flask, request, render_template_string
import base64

app = Flask(__name__)

# Variable to store the latest image
latest_image = None

# Route to handle image upload
@app.route('/image', methods=['POST'])
def upload_image():
    global latest_image
    data = request.json
    if 'image' in data:
        latest_image = data['image']
        return "Image received", 200
    else:
        return "No image found in request", 400

# Route to display the latest image
@app.route('/')
def display_image():
    if latest_image:
        # Render the latest image in an HTML template
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Latest Image</title>
        </head>
        <body>
            <h1>Latest Image</h1>
            <img src="data:image/jpeg;base64,{latest_image}" alt="Latest Image"/>
        </body>
        </html>
        """
        return render_template_string(html_template)
    else:
        return "No image available yet."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
