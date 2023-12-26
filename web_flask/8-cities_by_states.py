#!/usr/bin/python3

"""
Starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State & city objects"""
    states = storage.all(State)
    ret = []
    sorted_states = dict(sorted(states.items(), key=lambda x: x[1]['name']))
    for state in sorted_states.items():
        state = dict(state[1])
        ret.append(state)
    cities = storage.all(City)
    ret_cities = []
    sorted_cities = dict(sorted(cities.items(), key=lambda x: x[1]['name']))
    for city in sorted_cities.items():
        city = dict(city[1])
        ret_cities.append(city)
    return render_template('8-cities_by_states.html', data=ret, cities=ret_cities)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
