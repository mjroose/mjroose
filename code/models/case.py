from db import db

class CaseModel(db.Model):
    __tablename__ = 'cases'

    # TODO: add client, attorney, and charges
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(21))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship('ClientModel')

    # TODO:  add cases, attorneys, documents

    def __init__(self, number, client_id):
        self.number = number
        self.client_id = client_id
    
    def json(self):
        return {
            'client_id': self.client_id,
            'number': self.number
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_in_db(self, data):
        self.query.filter_by(id=self.id).update(data)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()