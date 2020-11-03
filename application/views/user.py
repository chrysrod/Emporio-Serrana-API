from flask import Blueprint, jsonify
from ..models.database import Firestore

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/users/get_users', methods=['GET'])
def get_users():

    res = Firestore().get_users()

    return jsonify(res)