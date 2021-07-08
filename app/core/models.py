from app import db
from sqlalchemy.dialects.postgresql import JSON


class TestModel(db.Model):
    __tablename__ = "TestTable"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Id: {self.id}"
