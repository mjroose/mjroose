from db import db
from utils.person import get_full_name

class ClientModel(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    middle_initial = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    full_name = db.Column(db.String(160))
    gender = db.Column(db.Boolean()) # False = Male; True = Female
    birthdate = db.Column(db.String(10))
    place_of_birth = db.Column(db.String(50))
    last_grade_completed = db.Column(db.String(30))
    citizen = db.Column(db.Boolean())
    phone_number = db.Column(db.String(14))
    email = db.Column(db.String(80))
    address = db.Column(db.String(200))
    cases = db.relationship('CaseModel', lazy='dynamic')

    # TODO:  add cases, attorneys, documents, notes

    def __init__(self, first_name, middle_initial, last_name, gender, birthdate, place_of_birth, last_grade_completed, citizen, phone_number, email, address):
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.full_name = get_full_name(first_name, middle_initial, last_name)
        self.gender = gender
        self.birthdate = birthdate
        self.place_of_birth = place_of_birth
        self.last_grade_completed = last_grade_completed
        self.citizen = citizen
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'middle_initial': self.middle_initial,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'gender': self.gender,
            'birthdate': self.birthdate,
            'place_of_birth': self.place_of_birth,
            'last_grade_completed': self.last_grade_completed,
            'citizen': self.citizen,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
            'case_ids': [case.id for case in self.cases]
        }
   
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_in_db(self, data):
        if self.first_name != data['first_name'] or self.middle_initial != data['middle_initial'] or self.last_name != data['last_name']:
            data['full_name'] = get_full_name(data['first_name'], data['middle_initial'], data['last_name'])

        self.query.filter_by(id=self.id).update(data)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def all(cls):
        return cls.query.all()