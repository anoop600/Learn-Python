"""
from flask import Flask
from flask_restful import Api
from add import Add
from subtract import Subtract
from multiply import Multiply
from divide import Divide
from visit_count import Visit

# Initialize FLASK app
app = Flask(__name__)
# Initialize RestFul API for the flask App
api = Api(app)


# REST-API-Controller
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")
api.add_resource(Visit, "/hello")


@app.route('/')
def hello_world():
    return "Simple Calculator !"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import bcrypt
import os

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.sentences_database
users = db["users"]


def verify_pw(user_name, password):
    hashed_pw = users.find({
        "UserName": user_name
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def count_tokens(user_name):
    tokens = users.find({
        "UserName": user_name
    })[0]["Tokens"]
    return tokens


class Register(Resource):
    def post(self):
        # Step 1: get posted data
        posted_data = request.get_json()

        # Step 2: Get data
        user_name = posted_data["user_name"]
        password = posted_data["password"]
        print(user_name)
        print(password)
        # Step 3: (Hash + salt) password and Store data
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(12))

        print(hashed_pw)
        users.insert_one({
            "UserName": user_name,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 6
        })

        return_json = {
            "status": 200,
            "msg": "You Successfully signed up for the API"
        }
        return jsonify(return_json)


class Store(Resource):
    def post(self):
        # Step 1 :get the posted data
        posted_data = request.get_json()

        # Step2 :is to read the data
        user_name = posted_data["user_name"]
        password = posted_data["password"]
        sentence = posted_data["sentence"]

        # Step 3:Verify the username pw match
        correct_pw = verify_pw(user_name, password)

        if not correct_pw:
            return_json = {
                "status": 302
            }
            return jsonify(return_json)
        # Step 4: Verify user has enough tokens
        num_tokens = count_tokens(user_name)
        if num_tokens <= 0:
            return_json = {
                "status": 301
            }
            return jsonify(return_json)

        # Step 5: Store the sentence take one token away and return 200
        users.update({
            "UserName": user_name
        }, {
            "$set": {
                "Sentence": sentence,
                "Tokens": num_tokens-1
            }
        })
        return_json = {
            "status": 200,
            "msg": "Sentence saved successfully"
        }
        return jsonify(return_json)

api.add_resource(Register, "/register")
api.add_resource(Store, "/store")
