from flask import request
from flask_restful import  Resource
from db_string import users
from helper import user_exist, generate_return_dictionary
import bcrypt

class Register(Resource):
    def post(self):
        posted_data = request.get_json()
        user_name = posted_data["user_name"]
        password = posted_data["password"]

        if user_exist(user_name):
            return_json = generate_return_dictionary(301, "Invalid Username")
            return return_json

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            "user_name": user_name,
            "password": hashed_pw,
            "own": 0,
            "debt": 0
        })

        return_json = generate_return_dictionary(
            200, "You have Successfully signed up for the API")
        return return_json