import json
import uuid

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from app import db
from app.user.models import User

user_controller = Blueprint('user', __name__)


@user_controller.route('', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        output.append(user.serialize)
    return jsonify({'users': output})


@user_controller.route('/<public_id>', methods=['GET'])
def get_one_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'No user found!'}), 400

    return jsonify({'user': user.serialize})


@user_controller.route('', methods=['POST'])
def create_user():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    test = User(**json.loads(json.dumps(request.json)))
    test.public_id = str(uuid.uuid4())
    test.password = hashed_password
    test.admin = False
    db.session.add(test)
    db.session.commit()
    return ''


@user_controller.route('/<public_id>', methods=['PUT'])
def update_user():
    return ''


@user_controller.route('/<public_id>', methods=['DELETE'])
def delete_user():
    return ''
