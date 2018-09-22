import os
import face_recognition
import numpy
import pickle

def save_person(face, name):
    path="./faces"+'/'+name
    try:
        os.mkdir(path)
    except FileExistsError as e:
        pass
    try:
        number = ([int((str((row.split('.'))[0]).split('_'))[1]) for row in os.listdir(path) if row!=name])
        last_index = max(number)
    except ValueError as e:
        last_index = 0
    last_index = int(last_index) +1
    filename = path+'/'+name+'_'+str(last_index)+'.png'
    face.save(filename)
    try:
        one_face_encoding =face_recognition.face_encodings(numpy.array(face))[0]

        with open(path+'/'+name, 'ab') as file:
            my_pickler = pickle.Pickler(file)
            my_pickler.dump(list(one_face_encoding))
    except IndexError as e:
        pass