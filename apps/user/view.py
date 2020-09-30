from flask import Blueprint, url_for
from flask_restful import Resource, fields, marshal_with, reqparse, inputs, marshal

from apps.user.model import User
from exts import api, db

user_bp = Blueprint('user', __name__, url_prefix='/api')


class IsTester(fields.Raw):
    def format(self, value):
        return 'tester'


user_fields = {
    'id': fields.Integer,
    'private_name': fields.String(attribute='username'),
    'password': fields.String,
    'tester': IsTester(attribute='username'),
    'updatetime': fields.DateTime
}

user_friends_fields = {
    'username': fields.String,
    'nums': fields.Integer,
    'friends': fields.List(fields.Nested(user_fields))
}

parse = reqparse.RequestParser(bundle_errors=True)
parse.add_argument('username', type=str, required=True, help='必须输入用户名', location=['form'])
parse.add_argument('password', type=inputs.regex(r'^\d{6,12}$'), required=True, help='必须输入用户名', location=['form'])
parse.add_argument('hobby', action='append', location=['form'])


# 类视图
class UserResource(Resource):
    # get 请求的处理
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        return users

    @marshal_with(user_fields)
    def post(self):
        args = parse.parse_args()
        username = args.get('username')
        password = args.get('password')
        hobby = args.get('hobby')
        print(hobby)
        user = User()
        user.username = username
        user.password = password
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self):
        return {'msg': '-----delete'}

    def put(self):
        return {'msg': '-----put'}


class UserSimpleResource(Resource):
    @marshal_with(user_fields)
    def get(self, uid):
        user = User.query.get(uid)
        print(user)
        return user

    def post(self, uid):
        print('endpoint的使用', url_for('all_user'))
        return {'msg': 'ok'}

    def delete(self, uid):
        return {'msg': '-----delete'}

    def put(self, uid):
        return {'msg': '-----put'}


class UserFriendSResource(Resource):
    @marshal_with(user_friends_fields)
    def get(self, uid):
        user = User.query.get(uid)
        friends = User.query.all()

        friend_list = []
        for friend in friends:
            friend_list.append(friend)

        data = {
            'username': user.username,
            'nums': len(friend_list),
            # 'friends': marshal(friend_list, user_fields)
            'friends': friend_list
        }

        return data


api.add_resource(UserResource, '/user', endpoint='all_user')
api.add_resource(UserSimpleResource, '/users/<int:uid>')
api.add_resource(UserFriendSResource, '/friends/<int:uid>')
