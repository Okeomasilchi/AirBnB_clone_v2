#!/usr/bin/python3

"""
starts a Flask web application:
listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
