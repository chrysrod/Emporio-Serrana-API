from application.views.auth import auth_bp
from application.views.user import user_bp
from flask import Flask
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 80)))