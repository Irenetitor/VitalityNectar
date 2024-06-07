#Flask-Sqlalchemy model class
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, TIMESTAMP

db = SQLAlchemy()

class Smoothies(db.Model):
    recid = db.Column(db.Integer, primary_key=True)
    recipename = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    image = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"User(recid={self.recid}, recipename={self.recipename}, image={self.image})"