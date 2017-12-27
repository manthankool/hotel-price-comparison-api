import os


from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate , identity
from resources.user import UserRegister
from resources.item import Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
api = Api(app)
app.secret_key = 'manthan'



jwt = JWT(app , authenticate , identity)




api.add_resource(Item , '/item/<string:city>')

api.add_resource(UserRegister, '/register')



if __name__ == '__main__':
    from db import db  #we are importing it here because of circular imports
    db.init_app(app)
    app.run(port=5000, debug = True)
