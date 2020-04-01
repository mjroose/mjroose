from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.case import CaseModel
from models.user import UserModel
from parsers.case import case_parser

# TODO:  Add JWT requirement

class Case(Resource):
    def get(self, _id):
        case = CaseModel.find_by_id(_id)
        if case:
            return case.json()
        return {'message': 'Case not found.'}, 404
    
    def delete(self, _id):
        case = CaseModel.find_by_id(_id)
        if case:
            case.delete_from_db()

        return {'message': 'Case deleted.'}
    
    def put(self, _id):
        case = CaseModel.find_by_id(_id)

        if case is None:
            return {'message': 'Unable to locate a case with that id.'}, 404

        data = case_parser.parse_args()
        data['attorneys'] = [attorney for attorney in UserModel.all_attorneys() if attorney.id in data['attorney_ids']]
        del data['attorney_ids']

        case.update_in_db(data)

        return case.json()

class CaseList(Resource):
    def get(self):
        return {'cases': [case.json() for case in CaseModel.query.all()]}

    def post(self):
        data = case_parser.parse_args()
        data['attorneys'] = [attorney for attorney in UserModel.all_attorneys() if data['attorney_ids'] is not None and attorney.id in data['attorney_ids']]
        del data['attorney_ids']
        
        case = CaseModel(**data)

        try:
            case.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500
        return case.json(), 201