#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def displays_python(text=None):
    """display "Python", followed by the value of the text variable"""
    if text is None:
       text = 'is cool'
    x = text
    if "_" in text:
        x = text.replace('_', ' ')
    return "Python {}".format(escape(x))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
