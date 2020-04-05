from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.service_document import ServiceDocumentModel
from parsers.service_document import service_document_parser

# TODO:  Add JWT requirement

class ServiceDocument(Resource):
    def get(self, _id):
        service_document = ServiceDocumentModel.find_by_id(_id)
        if service_document:
            return service_document.json()
        return {'message': 'Service document not found.'}, 404
    
    def delete(self, _id):
        service_docuemnt = ServiceDocumentModel.find_by_id(_id)
        if service_docuemnt:
            service_docuemnt.delete_from_db()

        return {'message': 'Service document deleted.'}
    
    def put(self, _id):
        service_document = ServiceDocumentModel.find_by_id(_id)

        if service_document is None:
            return {'message': 'Unable to locate a service document with that id.'}, 404

        data = service_document_parser.parse_args()

        service_document.update_in_db(data)

        return service_document.json()

class ServiceDocumentList(Resource):
    def get(self):
        return {'service_documents': [service_document.json() for service_document in ServiceDocumentModel.query.all()]}

    def post(self):
        data = service_document_parser.parse_args()
        service_document = ServiceDocumentModel(**data)

        try:
            service_document.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item.'}, 500
        return service_document.json(), 201