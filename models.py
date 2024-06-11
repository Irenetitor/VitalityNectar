#Flask-Sqlalchemy model class
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, TIMESTAMP

db = SQLAlchemy()

class Smoothies(db.Model):
    recid = db.Column(db.Integer, primary_key=True)
    recipename = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rest = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)    

    def __repr__(self) -> str:
        return f"Smoothie(recid={self.recid}, recipename={self.recipename}, image={self.image})"

class Benefits(db.Model):
    benid = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"Benefit(benid={self.benid}, tittle={self.tittle}, description={self.description})"   

class Favourites(db.Model):
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recid = db.Column(db.Integer, db.ForeignKey('smoothies.recid'), nullable=False)
    
    def __repr__(self) -> str:
        return f"Favourites(fid={self.fid}, recid={self.recid})"
    
class Contact(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    def __repr__(self) -> str:
        return f"Contact(cid={self.cid}, name={self.name}, email={self.email}, message={self.message})"
    
class Feedback(db.Model):
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    
    def __repr__(self) -> str:
        return f"Feedback(fid={self.fid}, name={self.name}, feedback={self.feedback})"