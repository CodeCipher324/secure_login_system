from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt

auth = Blueprint('auth', __name__)  # ✅ Define Blueprint before using it
bcrypt = Bcrypt()

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    user = User.query.filter_by(email=email).first()

    # Check if the account is locked
    if user and user.locked_until and user.locked_until > datetime.utcnow():
        return jsonify({"error": "Account locked. Try again later."}), 403

    if not user or not bcrypt.check_password_hash(user.password, password):
        if user:
            user.failed_attempts += 1
            # Lock account for 10 minutes after 5 failed attempts
            if user.failed_attempts >= 5:
                user.locked_until = datetime.utcnow() + timedelta(minutes=10)
                db.session.commit()
                return jsonify({"error": "Too many failed attempts. Account locked for 10 minutes."}), 403
            db.session.commit()
        return jsonify({"error": "Invalid credentials"}), 401

    # Reset failed attempts on successful login
    user.failed_attempts = 0
    user.locked_until = None
    db.session.commit()

    access_token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify({"access_token": access_token, "role": user.role}), 200


