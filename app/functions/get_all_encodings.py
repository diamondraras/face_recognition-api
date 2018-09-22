import os
import pickle

def get_all_encodings():

    path="./faces/"
    try:
        names = [row for row in os.listdir(path) if not(os.path.isfile(path+"/"+row))]
    except FileNotFoundError as e:
        os.mkdir(path)
    names = [row for row in os.listdir(path) if not(os.path.isfile(path+"/"+row))]
    encodings = list()
    for name in names:
        try:

            with open(path+'/'+name+'/'+name, 'rb') as file:
                temp = list()
                my_depickler = pickle.Unpickler(file)
                try:
                    while True:
                        temp.append(my_depickler.load())
                except EOFError as e:
                    pass
                encodings.append((name, temp))
        except FileNotFoundError as e:
            pass
    return encodings