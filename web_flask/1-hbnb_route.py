#!/usr/bin/python3

"""
starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""


from web_flask import app


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
