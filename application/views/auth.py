from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():

    res = {
        'status': 200,
        'endpoint': '/login'
    }

    return jsonify(res)

@auth_bp.route('/logout', methods=['POST'])
def logout():

    res = {
        'status': 200,
        'endpoint': '/logout'
    }

    return jsonify(res)
