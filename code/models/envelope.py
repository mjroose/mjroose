from db import db
from models.case import CaseModel

class EnvelopeModel(db.Model):
    __tablename__ = 'envelopes'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'))
    case = db.relationship('CaseModel')
    date_received = db.Column(db.String(16))

    # TODO:  add cases, attorneys, documents

    def __init__(self, number, case_id, date_received):
        self.number = number
        self.case_id = case_id
        self.date_received = date_received
    
    def json(self):
        return {
            'id': self.id,
            'number': self.number,
            'case_id': self.case.id,
            'date_received': self.date_received
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

    @classmethod
    def all(cls):
        return cls.query.all()