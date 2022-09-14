#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from markupsafe import escape
import re

# ...

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def flask():
    """
    Define route '/'
    return a string
    with method get
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    route define to '/hbnb'
    return a string
    with method get
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cisfun(text):
    """
    route define to '/c/<text>'
    display “C ” followed by
    the value of the text
    with method get
    """
    replaced_text = text.replace("_", " ")
    return 'C {}'.format(escape(replaced_text))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def Python(text):
    """
    route define to '/python/(<text>)'
    display “Python ”, followed by
    the value of the text
    with method get
    """
    replaced_text = text.replace("_", " ")
    options = ['is cool']
    for item in options:
        if text is item:
            return 'Python {}'.format(escape(text))
        else:
            return 'Python {}'.format(escape(replaced_text))


@app.route('/number/<int:n>/', strict_slashes=False)
def number(n):
    """
    route define to '/number/<n>'
    display n is a number”
    only if n is an integer
    with method get
    """
    if type(n) is int:
        return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
