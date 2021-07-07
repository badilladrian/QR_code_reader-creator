from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS

# Define the WSGI application object
app = Flask(__name__)

# REST API setup
api = Api(app)

# CORS setup
CORS(app)


# Configurations
# app.config.from_object('config')

# @app.route("/")
# def hello():
#     return "Hello, World!"