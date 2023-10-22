#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def all():
    """displays 10-hbnb_filters.html"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", amen=amenities, state=states)


@app.teardown_appcontext
def teardown(exc):
    """close the database"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
