from app import api
from app.core.views import HelloWorld

api.add_resource(HelloWorld, "/")