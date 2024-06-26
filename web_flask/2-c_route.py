#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask

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
def index2(text):
    """ here """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
