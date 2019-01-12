from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    script = db.Column(db.String(50))
    username = db.Column(db.String(255))

    def __init__(self, rating, script, username):
        self.rating = rating
        self.script = script
        self.username = username


 class RatingSchema(ma.Schema):
     class Meta:
         fields = ("id", "rating", "scrpt", "username")   


rating_schema = RatingSchema(strict=True)
ratings_schema = RatingSchema(many=True, strict=True)


if __name__ == "__main__":
    app.run(debug=True)