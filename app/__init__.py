from flask import Flask
from app.routes.recognize import Recognize
from app.routes.save import Save
from app.routes.get_all_faces import Get_all_faces

def create_app():
    _app = Flask(__name__)
    _app.secret_key = 'smart_house_secret_key'
    
    Recognize(_app)
    Save(_app)
    Get_all_faces(_app)

    
    return _app