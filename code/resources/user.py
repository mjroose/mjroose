from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email',
            type=str,
            required=True,
            help="The email field cannot be left blank!"
        )
        parser.add_argument('password',
            type=str,
            required=True,
            help="The password field cannot be left blank!"        
        )
        parser.add_argument('role',
            type=str,
            required=True,
            help="The role field cannot be left blank!")

        data = parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "User already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
