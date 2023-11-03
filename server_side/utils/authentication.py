# auth.py
from flask import request
from functools import wraps
import jwt

# Secret key for JWT (you should generate a strong secret key)
SECRET_KEY = 'your_secret_key'

# Sample user data (replace with your own user data)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

# Token-based authentication decorator
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            try:
                # Verify the token using the secret key
                data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return {'message': 'Token has expired'}, 401
            except jwt.InvalidTokenError:
                return {'message': 'Invalid token'}, 401
        else:
            return {'message': 'Token is missing'}, 401
    return decorated_function

# Login function
def login(username, password):
    if username in users and users[username] == password:
        # Create a JWT token
        token = jwt.encode({'username': username}, SECRET_KEY, algorithm='HS256')
        return token
    else:
        return None
