import os
import secrets
from flask import Flask
from models import db
from auth import auth
from admin import admin
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS globally

# App Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', secrets.token_hex(32))  # Use environment variable or generate a random one

# reCAPTCHA Configurations
app.config['RECAPTCHA_SITE_KEY'] = '6LfQh-YqAAAAAMgVFrFl7k8_CZ-uOTgNpTQw9ZPs'
app.config['RECAPTCHA_SECRET_KEY'] = '6LfQh-YqAAAAAEPpYpVAo-RtRnIZAfLhJFgo97wq'

# Initialize Extensions
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth)  
app.register_blueprint(admin)

# Create Database Tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

