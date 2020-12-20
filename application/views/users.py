from flask import Blueprint, jsonify, make_response, request
from functools import wraps

from application.controllers.auth import Auth
from application.controllers.users import Users

users_bp = Blueprint('users', __name__)

def token_required(function):
    
    @wraps(function)
    def decorated(*args, **kwargs):

        if 'Authorization' in request.headers and request.headers['Authorization']:
            user_data = Auth().verify_token(request.headers['Authorization'])

            if not user_data:
                return make_response({'status': 401, 'message': 'Token is missing!'}, 401)
        
        else:
            return make_response({'status': 401,'message' : 'Token is missing!'}, 401)

        return function(user_data, *args, **kwargs)

    return decorated

@users_bp.route('/api/users/insert_user', methods=['POST'])
@token_required
def insert_user(user_data):
    req = request.get_json()

    response = Users().insert_user(req)

    return make_response(jsonify(response), 200)

@users_bp.route('/api/users/get_user', methods=['GET'])
@token_required
def get_user(user_data):
    
    username = request.args.get('username')
    response = Users().get_user(username)

    return make_response(jsonify(response), 200)

@users_bp.route('/api/users/get_all_users', methods=['GET'])
@token_required
def get_all_users(user_data):

    response = Users().get_all_users()

    return make_response(jsonify(response), 200)

@users_bp.route('/api/users/update_user', methods=['PUT'])
@token_required
def update_user(user_data):
    req = request.get_json()

    response = Users().update_user(req)

    return make_response(jsonify(response), 200)

@users_bp.route('/api/users/delete_user', methods=['DELETE'])
@token_required
def delete_user(user_data):
    req = request.get_json()

    username = req['username']
    response = Users().delete_user(username)

    return make_response(jsonify(response), 200)