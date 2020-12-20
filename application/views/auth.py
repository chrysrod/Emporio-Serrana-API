from flask import Blueprint, jsonify, make_response, request
from functools import wraps

from application.controllers.auth import Auth

auth_bp = Blueprint('auth', __name__)
auth = Auth()

def token_required(function):
    
    @wraps(function)
    def decorated(*args, **kwargs):

        if 'Authorization' in request.headers and request.headers['Authorization']:
            user_data = auth.verify_token(request.headers['Authorization'])

            if not user_data:
                return make_response({'status': 401, 'message': 'Token is missing!'}, 401)
        
        else:
            return make_response({'status': 401,'message' : 'Token is missing!'}, 401)

        return function(user_data, *args, **kwargs)

    return decorated

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    req = request.get_json()
    res = auth.login(req)

    return jsonify(res)

@auth_bp.route('/api/auth/logout', methods=['POST'])
@token_required
def logout(user_data):

    res = user_data

    return jsonify(res)
