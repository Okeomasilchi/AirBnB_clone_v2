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
    /number_odd_or_even/<n>: display a HTML page only
        if n is an integer: H1 tag: “Number: n is
        even|odd” inside the tag BODY
"""


from flask import Flask, render_template

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
    return f"Python {text.replace('_', ' ')}"


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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_even_odd(n):
    """
    takes a parameter n and checks if the number
    is an even or odd number.

    Args:
        n: The parameter "n" represents a number that
        is passed into the function.
    """
    number = None
    if int(n) % 2 == 0:
        number = f"{n} is even"
    else:
        number = f"{n} is odd"
    return render_template("6-number_odd_or_even.html", number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
