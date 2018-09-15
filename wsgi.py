from app import create_app

face_recognition_api = create_app()

if __name__ == '__main__':
    face_recognition_api.run(port=9999, host="0.0.0.0", debug=True)

