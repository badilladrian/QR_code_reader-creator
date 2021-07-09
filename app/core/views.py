from flask_restful import Resource
from app import app

class HelloWorld(Resource):
    def get(self):
        app.logger.info("working fine")
        return {"message": "Hello World!", "status": 200}
