from bcrypt import checkpw
from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(email, password):
    user = UserModel.find_by_email(email)
    if user and checkpw(password.encode('utf8'), user.password_hash):
        return user

def identity(payload):
    print(str(payload))
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)