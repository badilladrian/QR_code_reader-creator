from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import redis

from config import *

# Define the WSGI application object
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# REST API setup
api = Api(app)

# CORS setup
CORS(app)

redis_config = redis.Redis(host="localhost", port=6379, db=0)


# Configurations
# app.config.from_object('config')

# @app.route("/")
# def hello():
#     return "Hello, World!"