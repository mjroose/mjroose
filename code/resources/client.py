from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.client import ClientModel
from models.user import UserModel
from parsers.client import client_parser

# TODO:  Add JWT requirement

class Client(Resource):
    def get(self, _id):
        client = ClientModel.find_by_id(_id)
        if client:
            return client.json()
        return {'message': 'Client not found.'}, 404
    
    def delete(self, _id):
        client = ClientModel.find_by_id(_id)
        if client:
            client.delete_from_db()
            return {'message': 'Client deleted.'}
        return {'message': 'Client with that id not found.'}
    
    def put(self, _id):
        client = ClientModel.find_by_id(_id)

        if client is None:
            return {'message': 'Unable to locate a client with that id.'}, 404

        data = client_parser.parse_args()
        data['attorneys'] = [attorney for attorney in UserModel.all_attorneys() if attorney.id in data['attorney_ids']]
        del data['attorney_ids']

        client.update_in_db(data)

        return client.json()

class ClientList(Resource):
    def get(self):
        return {'clients': [client.json() for client in ClientModel.query.all()]}

    def post(self):
        data = client_parser.parse_args()
        data['attorneys'] = [attorney for attorney in UserModel.all_attorneys() if data['attorney_ids'] is not None and attorney.id in data['attorney_ids']]
        del data['attorney_ids']

        client = ClientModel(**data)

        try:
            client.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500
        return client.json(), 201