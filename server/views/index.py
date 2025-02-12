"""
App index (main) view.

URLs include:
/
"""
import flask
import server
import requests
import json 


@server.app.route('/')
def show_index():
    """Display / route."""
    response = requests.get('https://api.openf1.org/v1/intervals')
    print(response.text)

    context = {
        "name": "F1 App"
    }
    return flask.jsonify(**context)

