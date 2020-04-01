from db import db

attorneys_clients = db.Table('attorneys_clients',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('client_id', db.Integer, db.ForeignKey('clients.id'), primary_key=True)
)