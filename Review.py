from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = "reviewdata"
    isbn = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    
    def __init__(self,isbn,email,comment,rating) :
        
        self.isbn = isbn
        self.email = email
        self.comment=comment
        self.rating = rating
     
    