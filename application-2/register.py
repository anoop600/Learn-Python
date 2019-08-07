from flask import jsonify, request
from db_String import users
from flask_restful import Resource
import bcrypt

class Register(Resource):
    def post(self):
        # Step 1: get posted data
        posted_data = request.get_json()

        # Step 2: Get data
        user_name = posted_data["user_name"]
        password = posted_data["password"]

        # Step 3: (Hash + salt) password and Store data
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(12))

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
