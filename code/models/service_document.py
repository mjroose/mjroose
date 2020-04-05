from db import db
from models.envelope import EnvelopeModel

class ServiceDocumentModel(db.Model):
    __tablename__ = 'service_docuemnts'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80))
    was_reviewed = db.Column(db.Boolean)
    envelope_id = db.Column(db.Integer, db.ForeignKey('envelopes.id'))
    envelope = db.relationship('EnvelopeModel')
    case = db.relationship('Envelope_Model', secondary=True)

    def __init__(self, description, was_reviewed, envelope_id):
        self.description = description
        self.was_reviewed = was_reviewed
        self.envelope_id = envelope_id
    
    def json(self):
        return {
            'id': self.id,
            'description': self.description,
            'was_reviewed': self.was_reviewed,
            'envelope_id': self.envelope_id
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