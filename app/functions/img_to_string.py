import base64
import io
from PIL import *

def img_to_string(image):
    imgBytArr = io.BytesIO()
    image.save(imgBytArr, format='PNG')
    string_image = base64.b64encode(imgBytArr.getvalue()).decode('ascii')
    return string_image
