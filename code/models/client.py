from db import db

class EnvelopeModel(db.Model):
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

    # TODO:  add cases, attorneys, documents

    def __init__(self, first_name, middle_initial, last_name, gender, birthdate, place_of_birth, last_grade_completed, citizen, phone_number, email, address):
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.full_name = self.get_full_name(first_name, middle_initial, last_name)
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
            'first_name': self.first_name,
            'middle_initial': self.middle_initial,
            'last_name': self.last_name,
            'gender': self.gender,
            'birthdate': self.birthdate,
            'place_of_birth': self.place_of_birth,
            'last_grade_completed': self.last_grade_completed,
            'citizen': self.citizen,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address
        }

    @classmethod
    def get_full_name(cls, first, middle, last):
        if middle is '':
            return '{} {}'.format(first, last)
        return '{} {} {}'.format(first, middle, last)
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter(id=_id).first()
    


