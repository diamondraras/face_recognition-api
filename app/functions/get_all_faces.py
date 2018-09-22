from app.functions.img_to_string import img_to_string
from PIL import Image
import os


def get_all_faces():
    path = "./faces/"
    names = [row for row in os.listdir(path) if not(os.path.isfile(path+"/"+row))]
    all_faces = list()
    for name in names:
        _p =path+'/'+name
        images_names = [row for row in os.listdir(_p) if row!=name]
        for image in images_names:
            all_faces.append({
                "name" : name,
                "string_img" :img_to_string(Image.open(_p+'/'+image))
            })
    return all_faces