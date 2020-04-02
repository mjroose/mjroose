from bcrypt import gensalt, hashpw

from db import db
from joins.attorneys_cases import attorneys_cases
from models.case import CaseModel
from models.client import ClientModel
from utils.person import get_full_name

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password_hash = db.Column(db.String(80))
    role = db.Column(db.String(10))
    first_name = db.Column(db.String(80))
    middle_initial = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    full_name = db.Column(db.String(160))
    attorney_number = db.Column(db.String(8))
    phone_number = db.Column(db.String(14))
    address = db.Column(db.String(200))
    cases = db.relationship('CaseModel', secondary=attorneys_cases, lazy='subquery')

    def __init__(self, email, password, role, first_name, middle_initial, last_name, attorney_number='', phone_number='', address=''):
        self.email = email
        self.password_hash = hashpw(password.encode('utf8'), gensalt())
        self.role = role
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.full_name = get_full_name(first_name, middle_initial, last_name)
        self.attorney_number = attorney_number
        self.phone_number = phone_number
        self.address = address
        self.cases = []
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        if self.role == 'Attorney':
            return {
                'id': self.id,
                'email': self.email,
                'role': self.role,
                'first_name': self.first_name,
                'middle_initial': self.middle_initial,
                'last_name': self.last_name,
                'full_name': self.full_name,
                'attorney_number': self.attorney_number,
                'phone_number': self.phone_number,
                'address': self.address,
                'case_ids': [case.id for case in self.cases]
            }
        else:
            return {
                'id': self.id,
                'email': self.email,
                'role': self.role,
                'first_name': self.first_name,
                'middle_initial': self.middle_initial,
                'last_name': self.last_name,
                'full_name': self.full_name,
            }

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_in_db(self, data):
        self.query.filter_by(id=self.id).update(data)
        db.session.commit()
    
    @classmethod
    def all_attorneys(cls):
        return [user for user in cls.query.all() if user.role == 'Attorney']

    @classmethod
    def attorney_case_list(cls, _id):
        CaseModel.filter_by_attorney(cls.find_by_id(_id))

    @classmethod
    def attorney_client_list(cls, _id):
        pass