#!/usr/bin/python3

"""
List of states
"""
from models import storage
from flask import Flask
from model.state import State
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """get data from storage engine"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_info():
    """display a HTML page inside the tag BODY"""
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
