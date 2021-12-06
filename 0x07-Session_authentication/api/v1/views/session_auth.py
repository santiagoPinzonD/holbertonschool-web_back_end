#!/usr/bin/env python3
""" session views
"""
import os
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_user():
    """ login """
    form_data = request.form

    if not form_data.get('email'):
        return jsonify({"error": "email missing"}), 400
    if not form_data.get('password'):
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': form_data.get('email')})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(form_data.get('password')):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    print(session_id)
    session_name = os.getenv('SESSION_NAME')

    session = jsonify(user[0].to_json())
    session.set_cookie(session_name, session_id)
    return session


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ Logout user """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
