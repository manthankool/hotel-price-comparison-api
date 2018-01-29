from models.user import UserModel

from models.freeuser import FreeUserModel




def authenticate(username , password):
    user = UserModel.find_by_username(username) #find_by_username gives you username object or None if it doesn't exist
    if (user is not None and user.password == password):
        return user
    user = FreeUserModel.find_by_username(username) #find_by_username gives you username object or None if it doesn't exist
    if (user is not None and user.password == password):
        return user


def identity(payload):
    user_id = payload['identity']
    j=UserModel.find_by_id(user_id)
    k=FreeUserModel.find_by_id(user_id)
    if j is not None :
        return j
    elif k is not None:
        return k
    else:
        return k
