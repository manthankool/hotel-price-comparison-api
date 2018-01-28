from models.freeuser import FreeUserModel


def auth(username , password):
    user = FreeUserModel.find_by_username(username) #find_by_username gives you username object or None if it doesn't exist
    if (user is not None and user.password == password):
        return user


def ident(payload):
    user_id = payload['identity']
    return FreeUserModel.find_by_id(user_id)
