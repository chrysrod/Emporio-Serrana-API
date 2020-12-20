from flask import Blueprint, jsonify, make_response, request
from functools import wraps

from application.controllers.auth import Auth
from application.controllers.sales import Sales

sales_bp = Blueprint('sales', __name__)

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

@sales_bp.route('/api/sales/insert_sale', methods=['POST'])
@token_required
def insert_sale(user_data):
    req = request.get_json()

    response = Sales().insert_sale(req)

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/get_sale', methods=['GET'])
@token_required
def get_sale(user_data):
    
    sale_id = request.args.get('id')
    response = Sales().get_sale(sale_id)

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/get_all_sales', methods=['GET'])
@token_required
def get_all_sales(user_data):

    response = Sales().get_all_sales()

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/get_all_week_sales', methods=['GET'])
@token_required
def get_all_week_sales(user_data):

    response = Sales().get_all_week_sales()

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/get_past_three_week_sales', methods=['GET'])
@token_required
def get_past_three_week_sales(user_data):

    response = Sales().get_past_three_week_sales()

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/update_sale', methods=['PUT'])
@token_required
def update_sale(user_data):
    req = request.get_json()

    response = Sales().update_sale(req)

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/delete_sale', methods=['DELETE'])
@token_required
def delete_sale(user_data):
    req = request.get_json()

    sale_id = req['id']
    response = Sales().delete_sale(sale_id)

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/get_percentages', methods=['GET'])
@token_required
def get_percentages(user_data):

    response = Sales().get_percentages()

    return make_response(jsonify(response), 200)

@sales_bp.route('/api/sales/get_earnings', methods=['GET'])
@token_required
def get_earnings(user_data):

    response = Sales().get_earnings()

    return make_response(jsonify(response), 200)