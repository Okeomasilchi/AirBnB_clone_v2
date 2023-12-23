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
    /python/<text>: display “Python ”, followed by the
        value of the text variable (replace underscore
        _ symbols with a space )
    /number/<n>: display “n is a number” only if n is
        an integer
"""


from web_flask import app
from flask import render_template

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

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    The python function takes an optional text
    parameter and returns a string "is cool" if no
    argument is provided.

    Args:
        text: A string that represents the text to
        be displayed. The default value is "is cool".
        Defaults to is cool

    Returns:
        str: "python + {text}"
    """
    return f"python {text.replace('_', ' ')}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    The function takes a parameter n and
    does something with it.

    Args:
        n: The parameter "n" represents a number that
        is passed into the function.
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    takes a parameter n and
    does something with it.

    Args:
        n: The parameter "n" represents a number that
        is passed into the function.
    """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
