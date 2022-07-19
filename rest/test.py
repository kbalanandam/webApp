# curl -v http://127.0.0.1:5000/api/users
# curl -d "{\"email\":\"sampath@gmail.com\",\"name\":\"Sampath\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/users/add
# curl -d "{\"title\":\"test oracle post\",\"user\":\"bala\",\"category\":\"Oracle\",\"body\":\"Oracle learning is always fun!\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/posts/add
#curl -d "{\"name\":\"anil\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/delete/user
# curl -d "{\"name\":\"Oracle\"}" -H "Content-Type: application/json" http://127.0.0.1:5000/api/category/add

from model import db, User, Post, Category, app
from flask import request, jsonify, make_response
import json

db.drop_all()
db.create_all()

