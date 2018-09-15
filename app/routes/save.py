from flask import request,jsonify
from app.functions.string_to_img import string_to_img
from app.functions.save_person import save_person

class Save():
    def __init__(self, app):
        @app.route('/save', methods = ['POST'])
        def save():
            data = request.get_json()
            for obj in data:
                if obj['name']:
                    image = string_to_img(obj['string_img'])
                    save_person(image, obj['name'])
            return jsonify({"done" : True})