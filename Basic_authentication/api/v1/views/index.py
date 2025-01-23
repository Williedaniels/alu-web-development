#!/usr/bin/env python3
""" Index view module """
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ Unauthorized endpoint """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ Forbidden endpoint """
    abort(403)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ Status of the API """
    return jsonify({"status": "OK"})
