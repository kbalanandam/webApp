from model import db, User, Post, Category, app
import jwt
import hmac
import datetime
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import reqparse, Resource
from functools import wraps


class Auth(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user', type=str, required=True, help='user name cannot be blank')
        parser.add_argument('password', type=str, required=True, help='this cannot be blank')
        try:
            auth = parser.parse_args()
            _user = User.find_by_username(auth.user)
            if _user and hmac.compare_digest(_user.password, auth.password):
                token = jwt.encode(payload={'user': _user.user, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, key=app.config['SECRET_KEY'], algorithm='HS256')
                return {'token': token}, 201
            return {'messageType': 'Error', 'message': 'Wrong User name or Password !!'}, 403
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}, 500


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return {'messageType': 'Error', 'message': 'a valid token is missing'}

        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            current_user = User.query.filter_by(user=payload['user']).first()
        except jwt.InvalidTokenError:
            return {'messageType': 'Error', 'message': 'token is invalid'}
        except Exception as e:
            return {'messageType': 'Error', 'message': str(e)}
        return f(*args, **kwargs)
    return decorator

