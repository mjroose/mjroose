from flask_restful import Resource

from models.client import ClientModel
from models.user import UserModel
from parsers.user import user_parser

class User(Resource):
    def get(self, _id):
        user = UserModel.find_by_id(_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404
    
    def put(self, _id):
        user = UserModel.find_by_id(_id)

        if user is None:
            return {'message': 'Unable to locate a user with that id.'}, 404

        data = user_parser.parse_args()
        del data['password']
        
        user.update_in_db(data)

        return user.json()

    def delete(self, _id):
        user = UserModel.find_by_id(_id)
        if user:
            user.delete_from_db()

        return {'message': 'User deleted.'}

class UserRegister(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

    def post(self):
        data = user_parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "User already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
