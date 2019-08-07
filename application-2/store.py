from flask import jsonify, request
from pymongo import MongoClient
from helper import verify_pw, count_tokens
from db_String import users
from flask_restful import Resource
import bcrypt


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
