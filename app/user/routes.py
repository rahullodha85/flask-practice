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
    user = User(**json.loads(json.dumps(request.json)))
    user.public_id = str(uuid.uuid4())
    user.password = hashed_password
    user.admin = False
    db.session.add(user)
    db.session.commit()
    return jsonify({'Message': 'User %s created' % user.name})


@user_controller.route('/<public_id>', methods=['PUT'])
def update_user(public_id):
    data = request.json
    user = User.query.filter_by(public_id = public_id)
    if not user.first():
        return jsonify({'message': 'No user found!'}), 400
    user.update(data)
    db.session.commit()
    return jsonify({'Message': 'User %s updated' % data['name']})


@user_controller.route('/<public_id>', methods=['DELETE'])
def delete_user():
    return ''
