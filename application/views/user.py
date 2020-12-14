from flask import Blueprint, jsonify
from application.models.database import Firestore

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/users/get_all_users', methods=['GET'])
def get_all_users():

    res = Firestore().get_all_users()

    return jsonify(res)