import os
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)
    login_count = db.Column(db.Integer, default=0)

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the hash."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Converts user object to a dictionary (excluding password)."""
        data = {
            "username": self.username,
            "email": self.email,
            "login_count": self.login_count
        }
        data["created_at"] = self.created_at.isoformat() if self.created_at else None
        data["last_login"] = self.last_login.isoformat() if self.last_login else None
        return data


@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400

    username = data['username'].strip()
    password = data['password']
    email = data.get('email', '').strip()

    if not email:
        email = None

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    if email and User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 409

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    response_data = {
        "message": "Account created successfully!",
        "user": new_user.to_dict()
    }
    return jsonify(response_data), 201


@app.route('/api/signin', methods=['POST'])
def signin():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400

    username = data['username'].strip()
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401

    user.last_login = datetime.utcnow()
    user.login_count = user.login_count + 1
    db.session.commit()

    response_data = {
        "message": "Login successful!",
        "user": user.to_dict()
    }
    return jsonify(response_data), 200


@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users (passwords excluded)"""
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)

# The if __name__ == '__main__': block has been removed.
# Gunicorn will start the app directly.