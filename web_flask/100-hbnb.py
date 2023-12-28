#!/usr/bin/python3

"""
Starts a Flask web application
"""


from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


def sort_dict(Class, by="name"):
    """
    sorts a dictionary of classes based on a
    specified attribute and returns the sorted dictionary.

    Class: expected to be a dictionary where the
        keys are the names of the objects and the
        values are dictionaries containing attributes
        of the objects
    by: used to specify the key by which the dictionary
        should be sorted. By default, it is set to "name",
        which means the dictionary will be sorted by the
        values of the "name" key in ascending order.
        However, you can change the value of "by",
        defaults to name (optional)
    return: a sorted dictionary.
    """

    return dict(sorted(Class.items(), key=lambda x: x[1][by]))


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State & city objects"""
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    usrs = storage.all(User)

    ret = []
    ret_cities = []
    ret_amen = []
    ret_place = []
    users = []

    sorted_states = sort_dict(states)
    sorted_cities = sort_dict(cities)
    sorted_amen = sort_dict(amenities)
    sorted_place = sort_dict(places)
    sorted_usr = sort_dict(usrs, by="id")

    for state in sorted_states.items():
        state = dict(state[1])
        ret.append(state)

    for usr in sorted_usr.items():
        usr = dict(usr[1])
        users.append(usr)

    for place in sorted_place.items():
        place = dict(place[1])
        for us in users:
            if place["user_id"] == us["id"]:
                place['user_id'] = f"{us['first_name']} {us['last_name']}"
        
        ret_place.append(place)

    for amenity in sorted_amen.items():
        amenity = dict(amenity[1])
        ret_amen.append(amenity)

    for i in ret:
        for city in sorted_cities.items():
            city = dict(city[1])
            if city["state_id"] == i["id"]:
                ret_cities.append({"id": city['id'], "name": city['name']})
        i["cities"] = ret_cities
        ret_cities = []

    return render_template('100-hbnb.html', data=ret, amen=ret_amen, places=ret_place)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
