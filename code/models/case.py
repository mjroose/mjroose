from db import db
from joins.attorneys_cases import attorneys_cases
from models.client import ClientModel

class CaseModel(db.Model):
    __tablename__ = 'cases'

    # TODO: add client, attorney, and charges
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(21))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship('ClientModel')
    attorneys = db.relationship('UserModel', secondary=attorneys_cases, lazy='subquery')

    # TODO:  add cases, attorneys, documents

    def __init__(self, number, client_id, attorneys):
        self.number = number
        self.client = ClientModel.find_by_id(client_id)
        for attorney in attorneys:
            self.attorneys.append(attorney)
    
    def json(self):
        return {
            'id': self.id,
            'client_id': self.client.id,
            'number': self.number,
            'attorney_ids': [user.id for user in self.attorneys]
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_in_db(self, data):
        self.attorneys = data['attorneys']
        del data['attorneys']

        self.query.filter_by(id=self.id).update(data)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls):
        return cls.query.all()