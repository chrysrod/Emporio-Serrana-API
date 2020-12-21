from application.views.auth import auth_bp
from application.views.users import users_bp
from application.views.products import products_bp
from application.views.sales import sales_bp
from application.views.notifications import notifications_bp
from flask import Flask
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app)
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(products_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(notifications_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 80)))