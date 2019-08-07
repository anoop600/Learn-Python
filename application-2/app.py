from flask import Flask
from flask_restful import Api
from register import Register
from store import Store
from get_resource import Get


app = Flask(__name__)
api = Api(app)


api.add_resource(Register, "/register")
api.add_resource(Store, "/store")
api.add_resource(Get,"/getsentence")


if __name__ == "__main__":
    app.run(host="0.0.0.0")