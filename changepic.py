import os
import base64
from PIL import Image
import io

filed = open("return.txt","r")

for root, dirs, files in os.walk("\\"):
    for file in files:
        if file.endswith(".ico") or file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                base64_bytes = image_data = base64.b64decode(filed)
                image_stream = io.BytesIO(image_data)
                img = Image.open(image_stream)
                output_filename = os.path.abspath(file)
                icon_sizes = [(16, 16), (32, 32), (64, 64)]
                img.save(output_filename, format='ICO', sizes=icon_sizes)
                print("Replaced {} at {}".format(file,dirs))