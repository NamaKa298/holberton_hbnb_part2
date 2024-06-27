from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from API.v1.auth import auth as auth_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['JWT_SECRET_KEY'] = 'motdepasse'
app.register_blueprint(auth_blueprint, url_prefix='/auth')
db = SQLAlchemy(app)
jwt = JWTManager(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)