from models.user import UserModel





def authenticate(username , password):
    user = UserModel.find_by_username(username) #find_by_username gives you username object or None if it doesn't exist
    if (user is not None and user.password == password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
