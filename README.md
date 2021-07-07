# QR_reader-creator-Image_creator
This cam service will have 3 actions. One to scan QR codes, 2nd to take images pictures and finally generate a custom QR Code from the image.


## Installation

Follow the following process to setup the project:

* Create virtual environment by `python3 -m venv venv`
* Install all packages from requirements.txt file by `pip install -r requirements.txt`
* Run the Flask app by `python wsgi.py`
* In browser hit by `http://192.168.1.19:8080/`
* You'll show a response `{
    "message": "Hello World!",
    "status": 200
}`