from flask_restful import reqparse

service_document_parser = reqparse.RequestParser()
service_document_parser.add_argument('description',
    type=str,
    required=True,
    help="A service document must have a description!"
)
service_document_parser.add_argument('envelope_id',
    type=int,
    required=True,
    help="A service document must have an envelope_id!"
)
service_document_parser.add_argument('was_reviewed',
    type=bool,
    required=True,
    help="You must indicate whether the service document has been reviewed.")

