"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "shhhsecret"

connect_db(app)


@app.route("/api/cupcakes")
def list_cupcakes():
    """Returns all cupcakes in the system"""

    all_cupcakes = [cupcake.make_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Get request for finding a specific cupcake using id"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.make_dict())


@app.route("/api/cupcakes", methods=["POST"])
def make_cupcake():
    data = request.json
    cupcake = Cupcake(
        flavor=data["flavor"],
        rating=data["rating"],
        size=data["size"],
        image=data["image"] or None,
    )
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.make_dict()), 201)
