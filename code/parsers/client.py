from flask_restful import reqparse

client_parser = reqparse.RequestParser()
client_parser.add_argument('first_name',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('middle_initial',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('last_name',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('gender',
    type=bool,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('birthdate',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('place_of_birth',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('last_grade_completed',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('citizen',
    type=bool,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('phone_number',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('email',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('address',
    type=str,
    required=True,
    help="Fields cannot be left blank!"
)
client_parser.add_argument('attorney_ids',
    type=int,
    action='append',
    required=False
)