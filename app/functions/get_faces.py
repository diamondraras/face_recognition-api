from PIL import Image
import io
import face_recognition

def get_faces(new_image):
    img = Image.open(new_image)
    imgBytArr = io.BytesIO()
    img.save(imgBytArr, format='PNG')
    image = face_recognition.load_image_file(imgBytArr)
    face_locations = face_recognition.face_locations(image)
    image = Image.fromarray(image, 'RGB')
    faces = list()
    for face in face_locations:
        distance_x = face[1]-face[3]
        # distance_y = face[0]-face[2]
        param_crop = (face[1]-distance_x, face[0], face[3]+distance_x, face[2])
        cropped_img = image.crop(param_crop)
        faces.append(cropped_img)
    return faces