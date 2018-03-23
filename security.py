from model.User import UserModel

def authenticate(email, password):
    user = UserModel.find_by_email(email)
    if user and user.check_password(password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.query.get(user_id)