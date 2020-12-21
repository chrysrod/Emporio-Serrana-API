from base64 import b64encode, urlsafe_b64encode
from datetime import datetime, timedelta
from hashlib import sha512
from jwt import encode as jwt_encode, decode as jwt_decode

from application.controllers.users import Users
from application.models.database import Firestore

class Auth:

    def __init__(self):
        self.secret = 'zn1xct1RFpGvuyXC3E9BreRjVl9x1GxQ'
        self.users = Users()
        self.database = Firestore()

    def login(self, login_data):
        username = login_data['username']
        password = login_data['password']
        password_hash = sha512(password.encode('utf-8')).hexdigest()
        exp = datetime.utcnow() + timedelta(days=7)
    
        password_hash_database = self.users.get_user_password_hash(username)

        if password_hash_database:
            if password_hash == password_hash_database:
                payload = {'username': username, 'sub': 'emporioserrana.com.br', 'exp': exp}
                token = self.generate_token(payload)
                res = {'status': 200, 'message':'Login successful', 'token': token}
            else:
                res = {'status': 401, 'message': 'Incorrect password', 'token': ''}
        else:
            res = {'status': 401, 'message': 'User unauthorized', 'token': ''}

        return res

    def generate_token(self, user_data):
        token = jwt_encode(user_data, self.secret, algorithm='HS512').decode('utf-8')

        return token

    def verify_token(self, token):
        try:
            data = jwt_decode(token, self.secret, algorithms='HS512')
        except Exception:
            data = None

        return data