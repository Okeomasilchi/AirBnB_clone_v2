#!/usr/bin/python3

"""
starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of
        the text variable (replace underscore 
        _ symbols with a space )
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    returns the string "Hello HBNB!".

    Returns:
        str: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns the string "HBNB".

    Returns:
        str: "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """
    returns C followed by the value of the
        text variable (replacing underscore
        symbols with a space )

    Returns:
        str: "C + text"
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
