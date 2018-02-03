
import sqlite3
from flask_restful import Resource, reqparse
from models.freeuser import FreeUserModel
from flask import render_template
class FreeUserRegister(Resource):

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
        data = FreeUserRegister.parser.parse_args()

        if FreeUserModel.find_by_email(data['email']) or FreeUserModel.find_by_username(data['username']):
            return {"message": "A user with that email or username already exists"}, 400

        user = FreeUserModel(data['username'],data['email'],data['password'])
        user.save_to_db()

        return '<h1> Hey, welcome to MakCorps, Hope we can change the world together </h1>',201
