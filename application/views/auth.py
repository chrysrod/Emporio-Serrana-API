from flask import Blueprint, jsonify, request

from application.controllers.auth import Auth

auth_bp = Blueprint('auth', __name__)
auth = Auth()

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    req = request.get_json()
    res = auth.login(req)

    return jsonify(res)

@auth_bp.route('/api/auth/logout', methods=['POST'])
def logout():

    res = {
        'status': 200
    }

    return jsonify(res)
