#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """display "C" followed by the value of the text variable"""
    x = text
    if '_' in text:
        x = text.replace('_', ' ')
    return 'C {}'.format(escape(x))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
