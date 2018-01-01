import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
             type=str,
             required=True,
             help="this field cannot be left blank"
             )
    parser.add_argument('password',
          type=str,
          required=True,
          help="this field cannot be left blank"
          )
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"A user already exist with the same name"},400

        user = UserModel(**data)      #**data = data['username'], data['password']
        user.save_to_db()


        return {'message':'User created sucessfully'},201  #201 means created
