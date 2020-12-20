from application.models.database import Firestore

class Products:

    def __init__(self):
        self.database = Firestore()

    def insert_product(self, product_data):

        response = self.database.insert_product(product_data)
        
        return response

    def get_product(self, product_id):

        response = self.database.get_product(product_id)

        return response

    def get_all_products(self):

        response = self.database.get_all_products()

        return response

    def update_product(self, product_data):

        response = self.database.update_product(product_data)

        return response

    def delete_product(self, product_id):

        response = self.database.delete_product(product_id)

        return response