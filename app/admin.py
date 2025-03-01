from flask import Blueprint, jsonify
from models import db, User
from rbac import role_required  # Import role-based access control
from flask_jwt_extended import jwt_required

admin = Blueprint('admin', __name__)

@admin.route('/admin/dashboard', methods=['GET'])
@jwt_required()
@role_required("admin")
def admin_dashboard():
    users = User.query.all()
    users_data = [{"id": u.id, "username": u.username, "email": u.email, "role": u.role} for u in users]

    return jsonify({"users": users_data}), 200
