from flask import Flask
from flask_restful import Api
from register import Register
from store import Store


app = Flask(__name__)
api = Api(app)


api.add_resource(Register, "/register")
api.add_resource(Store, "/store")

