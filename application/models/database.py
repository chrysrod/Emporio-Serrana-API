import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firestore:

    def __init__(self, key='aurora-292021-5b660df57621.json'):
        cred = credentials.Certificate('application/keys/' + key)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_user_data(self, username):
        collection = 'users'
        document = username
        
        res = self.db.collection(collection).document(document).get().to_dict()

        return res

    def get_all_users(self):
        collection = 'users'
        
        docs = self.db.collection(collection).stream()
        res = [doc.to_dict() for doc in docs]

        return res

    def insert_user(self, data):
        collection = 'users'
        document = data['username']
        
        self.db.collection(collection).document(document).set(data)

    def update_user(self, data):
        collection = 'users'
        document = data['username']
        
        self.db.collection(collection).document(document).update(data)

    def delete_user(self, data):
        collection = 'users'
        document = data['username']
        
        self.db.collection(collection).document(document).delete()