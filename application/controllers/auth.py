import datetime
from jwt import encode as jwt_encode, decode as jwt_decode
from application.models.database import Firestore

from base64 import b64encode, urlsafe_b64encode

class Auth:

    def __init__(self):
        self.secret = 'zn1xct1RFpGvuyXC3E9BreRjVl9x1GxQ'
        self.database = Firestore()

    def login(self, login_data):
        username = login_data['username']
        password_hash = login_data['password']
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=7)
        
        user_data = self.database.get_user_data(username)

        if user_data:
            if password_hash == user_data['password_hash']:
                payload = {'username': username, 'exp': exp}
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
        data = jwt_decode(token, self.secret, algorithms='HS512')

        return data