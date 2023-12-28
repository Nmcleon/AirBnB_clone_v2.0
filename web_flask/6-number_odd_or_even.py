#!/usr/bin/python3

"""
Odd or even
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Add route /hbnb"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text=None):
    """display “C ” followed by value of the text var
    replace underscore _ symbols with a space """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """display “Python ”, followed by the value of text var
    replace underscore _ symbols with a space"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def only_number(n=None):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
