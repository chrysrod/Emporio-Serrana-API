from flask import Blueprint, jsonify, make_response, request
from functools import wraps

from application.controllers.auth import Auth
from application.controllers.notifications import Notifications

notifications_bp = Blueprint('notifications', __name__)

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

@notifications_bp.route('/api/notifications/get_products_close_to_expiration_date', methods=['GET'])
@token_required
def get_products_close_to_expiration_date(user_data):

    response = Notifications().get_products_close_to_expiration_date()

    return make_response(jsonify(response), 200)