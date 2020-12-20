from application.models.database import Firestore

class Users:

    def __init__(self):
        self.database = Firestore()

    def insert_user(self, user_data):

        response = self.database.insert_user(user_data)
        
        return response

    def get_user(self, username):
        
        response = self.database.get_user(username)
        
        return response

    def get_user_password_hash(self, username):

        response = self.database.get_user_password_hash(username)

        return response
    
    def get_all_users(self):

        response = self.database.get_all_users()
        
        return response
    
    def update_user(self, user_data):

        response = self.database.update_user(user_data)
        
        return response

    def delete_user(self, username):

        response = self.database.delete_user(username)

        return response