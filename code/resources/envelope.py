from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.case import CaseModel
from models.envelope import EnvelopeModel
from parsers.envelope import envelope_parser

# TODO:  Add JWT requirement

class Envelope(Resource):
    def get(self, _id):
        envelope = EnvelopeModel.find_by_id(_id)
        if envelope:
            return envelope.json()
        return {'message': 'Envelope not found.'}, 404
    
    def delete(self, _id):
        envelope = EnvelopeModel.find_by_id(_id)
        if envelope:
            envelope.delete_from_db()

        return {'message': 'Envelope deleted.'}
    
    def put(self, _id):
        envelope = EnvelopeModel.find_by_id(_id)

        if envelope is None:
            return {'message': 'Unable to locate a envelope with that id.'}, 404

        data = envelope_parser.parse_args()

        envelope.update_in_db(data)

        return envelope.json()

class EnvelopeList(Resource):
    def get(self):
        return {'envelopes': [envelope.json() for envelope in EnvelopeModel.query.all()]}

    def post(self):
        data = envelope_parser.parse_args()
        envelope = EnvelopeModel(**data)

        try:
            envelope.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500
        return envelope.json(), 201