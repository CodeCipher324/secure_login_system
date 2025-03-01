from flask import jsonify
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            verify_jwt_in_request()
            identity = get_jwt_identity()

            if not identity or identity.get("role") != required_role:
                return jsonify({"error": "Access denied. Admins only."}), 403

            return f(*args, **kwargs)
        return decorated_function
    return decorator
