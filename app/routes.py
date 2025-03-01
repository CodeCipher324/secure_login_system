import requests
from flask import Blueprint, request, jsonify, current_app
from models import db, User, bcrypt
from flask_jwt_extended import create_access_token

routes = Blueprint('routes', __name__)  # Create a blueprint for routes

@routes.route('/register', methods=['POST'])
def register():
    try:
        # Get data from JSON request
        data = request.json  
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'user')  # Default role is 'user'

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message": "User already exists"}), 400

        # Hash the password before storing
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create new user with hashed password
        new_user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@routes.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        recaptcha_response = data.get('recaptcha_response')

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Verify reCAPTCHA
        recaptcha_verify_url = "https://www.google.com/recaptcha/api/siteverify"
        recaptcha_data = {
            "secret": current_app.config['RECAPTCHA_PRIVATE_KEY'],  # Use current_app for app context
            "response": recaptcha_response
        }
        recaptcha_result = requests.post(recaptcha_verify_url, data=recaptcha_data).json()

        if not recaptcha_result.get("success"):
            return jsonify({"error": "reCAPTCHA verification failed"}), 403

        # Find the user
        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error": "Invalid credentials"}), 401

        # Generate JWT token
        access_token = create_access_token(identity={"id": user.id, "role": user.role})
        return jsonify({"access_token": access_token, "role": user.role}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

