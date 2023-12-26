#!/usr/bin/python3

"""
Starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State)
    ret = []
    sorted_states = dict(sorted(states.items(), key=lambda x: x[1]['name']))
    for state in sorted_states.items():
        state = dict(state[1])
        ret.append(state)
    return render_template('7-states_list.html', data=ret)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
