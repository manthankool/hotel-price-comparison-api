import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.contrib.fixers import ProxyFix



from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate , identity
from fsecurity import auth , ident
from resources.user import UserRegister
from resources.freeuser import FreeUserRegister

app = Flask(__name__)




app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'manthan'
api = Api(app)




app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
limiter = Limiter(
    app,
    key_func= get_remote_address
)
@app.before_first_request
def create_tables():
    db.create_all()
jwt = JWT(app , authenticate , identity)
fjwt = JWT(app, auth, ident)


from resources.item import Item
from resources.free import FreeItem
api.add_resource(Item , '/item/<string:city>')

api.add_resource(FreeItem , '/free/<string:city>')
api.add_resource(FreeUserRegister, '/freeregister')
api.add_resource(UserRegister, '/register')




from db import db
db.init_app(app)
app.run(port=5000,debug=True)
