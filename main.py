from application.views.auth import auth_bp
from application.views.user import user_bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)