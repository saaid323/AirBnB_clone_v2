#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def all():
    """displays 100-hbnb.html"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html", amen=amenities,
                           state=states, places=places)


@app.teardown_appcontext
def teardown(exception):
    """close the database"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
