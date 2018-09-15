from flask import request, jsonify
from app.functions.get_faces import get_faces
from app.functions.get_all_encodings import get_all_encodings
from app.functions.get_all_encodings import get_all_encodings
from app.functions.img_to_string import img_to_string
from PIL import Image
import io
import face_recognition
import sys
import numpy


# sys.path.append('../.')
class Recognize():
    def __init__(self, app):
        @app.route('/recognize', methods = ['POST'])
        def recognize():
            image = request.files['image']
            faces = get_faces(image)
            img = Image.open(image)
            imgBytArr = io.BytesIO()
            img.save(imgBytArr, format='PNG')
            image = face_recognition.load_image_file(imgBytArr)
            # face_locations = face_recognition.face_locations(image)
            encodings = get_all_encodings()
            string_faces = [img_to_string(face) for face in faces]
            response = []
            known = False
            for i,face in enumerate(faces):
                accuracies = list()
                for _inused,one_person_encoding in (encodings):
                    unknwon_face_encoding = face_recognition.face_encodings(numpy.array(face))[0]

                    matchs = face_recognition.compare_faces(one_person_encoding, unknwon_face_encoding,tolerance=0.4)
                    accuracy = len([row for row in matchs if row])/len(matchs)
                    accuracies.append(accuracy)
                    if accuracy!=0:
                        known = True
                if accuracies:
                    best_index = accuracies.index(max(accuracies))
                if known:
                    response.append({
                        "name" : encodings[best_index][0],
                        "string_img" : string_faces[i]
                    })
                else:
                    response.append({
                        "name" : "",
                        "string_img" : string_faces[i]
                    })

            return jsonify(response)