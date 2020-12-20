from flask import Blueprint, jsonify, make_response, request
from functools import wraps

from application.controllers.auth import Auth
from application.controllers.products import Products

products_bp = Blueprint('products', __name__)

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

@products_bp.route('/api/products/insert_product', methods=['POST'])
@token_required
def insert_product(user_data):
    req = request.get_json()

    response = Products().insert_product(req)

    return make_response(jsonify(response), 200)

@products_bp.route('/api/products/get_product', methods=['GET'])
@token_required
def get_product(user_data):
    
    product_id = request.args.get('id')
    response = Products().get_product(product_id)

    return make_response(jsonify(response), 200)

@products_bp.route('/api/products/get_all_products', methods=['GET'])
@token_required
def get_all_products(user_data):

    response = Products().get_all_products()

    return make_response(jsonify(response), 200)

@products_bp.route('/api/products/update_product', methods=['PUT'])
@token_required
def update_product(user_data):
    req = request.get_json()

    response = Products().update_product(req)

    return make_response(jsonify(response), 200)

@products_bp.route('/api/products/delete_product', methods=['DELETE'])
@token_required
def delete_user(user_data):
    req = request.get_json()

    product_id = req['id']
    response = Products().delete_product(product_id)

    return make_response(jsonify(response), 200)