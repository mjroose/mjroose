from db import db

attorneys_cases = db.Table('attorneys_cases',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('case_id', db.Integer, db.ForeignKey('cases.id'), primary_key=True)
)