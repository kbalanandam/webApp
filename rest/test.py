# curl -v http://127.0.0.1:5000/api/users
# curl -d "{\"email\":\"sampath@gmail.com\",\"name\":\"Sampath\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/users/add
# curl -d "{\"title\":\"test oracle post\",\"user\":\"bala\",\"category\":\"Go\",\"body\":\"Go learning is always fun!\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/posts
# curl -d "{\"name\":\"anil\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/delete/user
#curl  http://127.0.0.1:5000/api/categories/PowerBI -X DELETE
#curl -d "{\"name\":\"PowerBI\",\"description\":\"this is for PowerBI\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/categories

from model import db, User, Post, Category, app
from flask import request, jsonify, make_response
import json

#db.drop_all()
#db.create_all()

import functools
user = {"username": "Josh", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f"No admin access for this user {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return '1234'


#get_admin_password = make_secure(get_admin_password())
print(get_admin_password())


