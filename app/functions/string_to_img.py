import base64
import io
from PIL import Image

def string_to_img(str_img):
    b =bytes(str_img, "ascii")
    buf_image = io.BytesIO(base64.b64decode(b))
    return Image.open(buf_image)