from datetime import datetime, timedelta

from application.controllers.products import Products

class Notifications:

    def __init__(self):
        self.products = Products()

    def get_products_close_to_expiration_date(self):

        time_till = datetime.now() + timedelta(days=30)
        time_till_timestamp = datetime.timestamp(time_till)

        products = self.products.get_all_products()

        expiration_date_products = []

        for product in products:
            day = int(product['expiration_date'].split('/')[0])
            month = int(product['expiration_date'].split('/')[1])
            year = int(product['expiration_date'].split('/')[2])
            expiration_date = datetime.timestamp(datetime(year, month, day))
            if expiration_date <= time_till_timestamp:
                expiration_date_products.append(product)

        if expiration_date_products:
            response = {
                'message': 'The following products are close to the expiration date',
                'products': [product['name'] for product in expiration_date_products]
            }
        else:
            response = {
                'message': 'There are no products close to the expiration date'
            }

        return response