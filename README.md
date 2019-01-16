# face_recognition-api restful with python
A simple face_recgnition webservice api with flask

## Installation
Clone the repo and install requirements

```bash
$ pip install -r requirements.txt
```

Run the _wsgi.py_ file to start server

```bash
$ python wsgi.py
```

No server will be started on port _9999_
## Usage
1. To simply get and recognize faces in one image

```bash
$ curl -F 'image=@myImage.png' http://localhost:9999/recognize
```

If one or more faces were found, we get a json response (name and base64 image)

```json
[
    {
        "name" : "Diams",
        "string_img" : "iVBORw0KGgoAAAANSUhEUgAAAGsAAABrCAIAAAD/3etbAAA5WElEQVR4nHW9244kSZIldo6IqrlHXqq..."
    }

]
```

2. To simply save a known face

```bash
$ curl -H "Content-Type:application/json" -d "[{\"name\" : \"Diams\", string_img : \"iVBORw0KGgoAAAANSUhEUgAAAGsAAABrCAIAAAD/3etbAAA5WElEQVR4nHW9244kSZIldo6IqrlHXqq...\"}]
```

if there is no error the answer will be

```json
{
    "done": true
}
```

3. To simply get all known faces

```bash
$ curl http://localhost:9999/get_all_faces
```

the response return all saved faces

```json
[
    {
        "name" : "Voanjo",
        "string_img" : "iVBORw0KGgoAAAANSUhEUgAAAGsAAABrCAIAAAD/3etbAAA5WElEQVR4nHW9244kSZIldo6IqrlHXsdxqq..."
    },
    {
        "name" : "Ursulla",
        "string_img" : "iVBORw0KGgoAAAANSUhEUgAAAGwAAABsCAIAAAAABMCaAAA210lEQVR4nH29TY9kyZEtdo6Z3xuZ9dEfJJuc..."
    },
    {
        "name" : "Safdj",
        "string_img" : "iVBORw0KGgoAAAANSUhEUgAAAGwAAABrCAIAAAAdAfAiAABAeUlEQVR4nHX9Xa8tW3IdiI0RMWdmrrX2Pver..."
    }
    
]
```
