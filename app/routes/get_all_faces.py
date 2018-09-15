from app.functions.get_all_faces import get_all_faces
from flask import jsonify


class Get_all_faces :
    def __init__ (self, app):
        @app.route('/get_all_faces', methods = ['GET'])
        def get_all_faces_view():
            return jsonify(get_all_faces())
