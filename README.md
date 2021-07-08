# QR_reader-creator-Image_creator
This cam service will have 3 actions. One to scan QR codes, 2nd to take images pictures and finally generate a custom QR Code from the image.


## Installation

Follow the following process to setup the project:

* Create virtual environment by `python3 -m venv venv`
* Install all packages from requirements.txt file by `pip install -r requirements.txt`

## Database Setup
* create a file named `settings.json` and copy data from `settings_format.json` file
* Set Database name, user, password, port etc
* Run the following command to migrate db
* flask db init
* flask db migrate
* flask db upgrade
  
## System run
* Run the Flask app by `python wsgi.py`
* In browser hit by `http://192.168.1.19:8080/`
* You'll show a response `{
    "message": "Hello World!",
    "status": 200
}`
  
## Database Migration
Run the following command to migrate db

