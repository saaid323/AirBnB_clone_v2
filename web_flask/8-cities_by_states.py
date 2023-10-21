#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a HTML page"""
    state = storage.all(State)
    city = storage.all(City)
    return render_template('8-cities_by_states.html', city=city, state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
