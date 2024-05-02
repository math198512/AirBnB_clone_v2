#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ here """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ here """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """ here """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def ptext(text):
    """ here """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """ here """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number2(n):
    """ here """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
