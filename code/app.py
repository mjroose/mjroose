from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db
from security import authenticate, identity
from settings import APP_SECRET_KEY
from resources.case import Case, CaseList
from resources.client import Client, ClientList, ClientCaseList
from resources.user import User, UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = APP_SECRET_KEY
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)
# this creates a new route, /auth, that allows you to get an access token with a post request
# The header has to be Authorization: application/json
# The body has to be {"username": "bob", "password": "asdf"}
#
# This returns an access token.  Use the token by:
# Creating a header of Authorization: JWT ___access token___

api.add_resource(Case, '/case/<int:_id>')
api.add_resource(CaseList, '/cases')
api.add_resource(ClientCaseList, '/client/<int:client_id>/cases')
api.add_resource(Client, '/client/<int:_id>')
api.add_resource(ClientList, '/clients')
api.add_resource(User, '/user/<int:_id>')
api.add_resource(UserRegister, '/users')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)