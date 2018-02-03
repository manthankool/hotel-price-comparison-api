
import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(data['email']) or UserModel.find_by_username(data['username']):
            return {"message": "A user with that email or username already exists"}, 400

        user = UserModel(data['username'],data['email'],data['password'])
        user.save_to_db()

        return '<h1> Hey, welcome to MakCorps, Hope we can change the world together </h1>'
