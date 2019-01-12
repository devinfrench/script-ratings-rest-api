from flask import Flask, request, jsonify
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


@app.route("/ratings", methods=["GET"])
def get_all_ratings():
    ratings = Rating.query.all()
    result = ratings_schema.dump(ratings)
    return jsonify(result.data)


@app.route("/ratings/<script>", methods=["GET"])
def get_ratings(script):
    ratings = Rating.query.filter_by(script=script).all()
    result = ratings_schema.dump(ratings)
    return jsonify(result.data)


@app.route("/rating", methods=["POST"])
def create_rating():
    rating = request.json["rating"]
    script = request.json["script"]
    username = request.json["username"]
    new_rating = Rating(rating, script, username)
    db.session.add(new_rating)
    db.session.commit()
    return rating_schema.jsonify(new_rating)


@app.route("/rating", methods=["PUT"])
def update_rating():
    rating = Rating.query.filter_by(script=request.json["script"], username=request.json["username"]).first()
    rating.rating = request.json["rating"]
    sb.session.commit()
    return rating_schema.jsonify(rating)


@app.route("/rating", methods=["DELETE"])
def delete_rating():
    rating = Rating.query.filter_by(script=request.json["script"], username=request.json["username"]).first()
    db.session.delete(rating)
    db.session.commit()
    return rating_schema.jsonify(rating)


if __name__ == "__main__":
    app.run(debug=True)