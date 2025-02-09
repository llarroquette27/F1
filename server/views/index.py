"""
App index (main) view.

URLs include:
/
"""
import flask
import server


@server.app.route('/')
def show_index():
    """Display / route."""
    context = {
        "name": "F1 App"
    }
    return flask.jsonify(**context)

