from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from models import User
from extensions import db

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()


# Register User
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    # Check if email already exists
    existing_user = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing_user:
        return jsonify({
            "error": "Email already exists"
        }), 400

    # Hash password
    hashed_password = bcrypt.generate_password_hash(
        data["password"]
    ).decode("utf-8")

    # Create user
    user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password
    )

    # Save user
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


# Login User
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    # Find user by email
    user = User.query.filter_by(
        email=data["email"]
    ).first()

    # Validate email
    if not user:
        return jsonify({
            "error": "Invalid email or password"
        }), 401

    # Validate password
    if not bcrypt.check_password_hash(
        user.password,
        data["password"]
    ):
        return jsonify({
            "error": "Invalid email or password"
        }), 401

    # Generate JWT token
    access_token = create_access_token(
        identity=str(user.id)
    )

    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    }), 200


# Get Current Logged-in User
@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def get_me():
    # Get user ID from JWT token
    user_id = get_jwt_identity()

    # Find user in database
    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": str(user.created_at)
    }), 200