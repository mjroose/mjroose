from flask_restful import reqparse

envelope_parser = reqparse.RequestParser()
envelope_parser.add_argument('number',
    type=int,
    required=True,
    help="An envelope must have an envelope number!"
)
envelope_parser.add_argument('case_id',
    type=int,
    required=True,
    help="An envelope must have a case_id!"
)
envelope_parser.add_argument('date_received',
    type=str,
    required=True,
    help="An envelope must have a date received!"
)

