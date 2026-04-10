from flask import Flask, send_file
import random
import os

app = Flask(__name__)

IMAGE_FOLDER = 'images'

@app.route('/qr-code-image')
def qr_code_image():
    images = os.listdir(IMAGE_FOLDER)
    chosen_image = random.choice(images)
    return send_file(os.path.join(IMAGE_FOLDER, chosen_image))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)