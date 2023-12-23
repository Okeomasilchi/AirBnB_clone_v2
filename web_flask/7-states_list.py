#!/usr/bin/python3
"""
Starts a Flask web application
"""

from web_flask import app
from flask import render_template
from models import storage
from models.state import State
from os import environ


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State)
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    HBNB_MYSQL_USER = environ.get('HBNB_MYSQL_USER')
    HBNB_MYSQL_PWD = environ.get('HBNB_MYSQL_PWD')
    HBNB_MYSQL_HOST = environ.get('HBNB_MYSQL_HOST')
    HBNB_MYSQL_DB = environ.get('HBNB_MYSQL_DB')
    HBNB_TYPE_STORAGE = environ.get('HBNB_TYPE_STORAGE')

    app.run(host='0.0.0.0', port=5000)
