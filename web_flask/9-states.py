#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask, render_template, request
from models.state import State
from models.city import City
from models import storage
app = Flask(__name__)


@app.route('/states', methods=['GET'], strict_slashes=False)
def states_list():
    """display a HTML page"""
    states = storage.all(State).values()
    url = request.path
    no_id = True
    return render_template('9-states.html', no_id=no_id, states=states)


@app.route('/states/<id>', methods=['GET'], strict_slashes=False)
def states_city(id=None):
    """display a HTML page"""
    states = storage.all(State).values()
    i_id = True
    state = None
    for s in states:
        if s.id == id:
            state = s
    else:
        i_id = False
    return render_template('9-states.html', i_id=i_id, state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
