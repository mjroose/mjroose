from flask_restful import reqparse

user_parser = reqparse.RequestParser()
user_parser.add_argument('email',
    type=str,
    required=True,
    help="The email field cannot be left blank!"
)
user_parser.add_argument('password',
    type=str,
    required=True,
    help="The password field cannot be left blank!"        
)
user_parser.add_argument('role',
    type=str,
    required=True,
    help="The role field cannot be left blank!")
user_parser.add_argument('first_name',
    type=str,
    required=True,
    help="The first_name field cannot be left blank!")
user_parser.add_argument('middle_initial',
    type=str,
    required=True,
    help="The middle_initial field cannot be left blank!")
user_parser.add_argument('last_name',
    type=str,
    required=True,
    help="The last_name field cannot be left blank!")
user_parser.add_argument('attorney_number',
    type=str,
    required=False,
    help="There was a problem with the attorney_number field.")
user_parser.add_argument('phone_number',
    type=str,
    required=False,
    help="There was a problem with the phone_number field.")
user_parser.add_argument('address',
    type=str,
    required=False,
    help="There was a problem with the address field.")