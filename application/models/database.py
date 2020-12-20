import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firestore:

    def __init__(self, key='aurora-292021-5b660df57621.json'):
        
        try:
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate('application/keys/' + key)
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def insert_user(self, user_data):
        collection = 'users'
        document = user_data['username']
        
        user_ref = self.db.collection(collection).document(document)
        user_ref.set(user_data)

        response = {'status': 200, 'message': 'User successfully inserted'}

        return response

    def get_user(self, username):
        collection = 'users'
        document = username
        
        user = self.db.collection(collection).document(document).get().to_dict()

        response = {}

        if user:
            for data in user:
                if data != 'password_hash':
                    response[data] = user[data]

        return response

    def get_user_password_hash(self, username):
        collection = 'users'
        document = username

        user_data = self.db.collection(collection).document(document).get().to_dict()
        
        response = user_data['password_hash'] if 'password_hash' in user_data else None

        return response

    def get_all_users(self):
        collection = 'users'
        
        docs = self.db.collection(collection).stream()
        users = [doc.to_dict() for doc in docs]

        response = []

        for user in users:
            user_data = {}
            for data in user:
                if data != 'password_hash':
                    user_data[data] = user[data]
            response.append(user_data)

        return response

    def update_user(self, user_data):
        collection = 'users'
        document = user_data['username']
        
        if self.get_user(document):
            self.db.collection(collection).document(document).update(user_data)
            response = {'status': 200, 'message': 'User successfully updated'}
        else:
            response = {'status': 404, 'message': 'User not founded on database'}

        return response

    def delete_user(self, username):
        collection = 'users'
        document = username
        
        if self.get_user(document):
            self.db.collection(collection).document(document).delete()
            response = {'status': 200, 'message': 'User successfully deleted'}
        else:
            response = {'status': 404, 'message': 'User not founded on database'}

        return response

    def insert_product(self, product_data):
        collection = 'products'
        document = product_data['id']
        
        product_ref = self.db.collection(collection).document(document)
        product_ref.set(product_data)

        response = {'status': 200, 'message': 'Product successfully inserted'}

        return response

    def get_product(self, product_id):
        collection = 'products'
        document = product_id
        
        response = self.db.collection(collection).document(document).get().to_dict()

        return response

    def get_all_products(self):
        collection = 'products'
        
        docs = self.db.collection(collection).stream()
        response = [doc.to_dict() for doc in docs]

        return response

    def update_product(self, product_data):
        collection = 'products'
        document = product_data['id']
        
        if self.get_product(document):
            self.db.collection(collection).document(document).update(product_data)
            response = {'status': 200, 'message': 'Product successfully updated'}
        else:
            response = {'status': 404, 'message': 'Product not founded on database'}

        return response

    def delete_product(self, product_id):
        collection = 'products'
        document = product_id
        
        if self.get_product(document):
            self.db.collection(collection).document(document).delete()
            response = {'status': 200, 'message': 'Product successfully deleted'}
        else:
            response = {'status': 404, 'message': 'Product not founded on database'}

        return response

    def insert_sale(self, sale_data):
        collection = 'sales'
        
        product_ref = self.db.collection(collection).document()
        product_ref.set(sale_data)

        response = {'status': 200, 'message': 'Sale successfully inserted'}

        return response

    def get_sale(self, sale_id):
        collection = 'sales'
        document = sale_id
        
        response = self.db.collection(collection).document(document).get().to_dict()

        return response

    def get_all_sales(self):
        collection = 'sales'
        
        docs = self.db.collection(collection).stream()
        response = [doc.to_dict() for doc in docs]

        return response

    def get_week_sales_by_timestamp(self, time_from, time_till):
        collection = 'sales'
        
        docs = self.db.collection(collection).where('timestamp', '>=', time_from).where(
                                                    'timestamp', '<=', time_till).stream()
        
        response = [doc.to_dict() for doc in docs]

        return response

    def update_sale(self, sale_data):
        collection = 'sales'
        document = sale_data['id']
        
        if self.get_sale(document):
            self.db.collection(collection).document(document).update(sale_data)
            response = {'status': 200, 'message': 'Sale successfully updated'}
        else:
            response = {'status': 404, 'message': 'Sale not founded on database'}

        return response

    def delete_sale(self, sale_id):
        collection = 'sales'
        document = sale_id
        
        if self.get_sale(document):
            self.db.collection(collection).document(document).delete()
            response = {'status': 200, 'message': 'Sale successfully deleted'}
        else:
            response = {'status': 404, 'message': 'Sale not founded on database'}

        return response

    def get_percentages(self):
        collection = 'percentages'

        docs = self.db.collection(collection).stream()

        response = [doc.to_dict() for doc in docs]

        return response