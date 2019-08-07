from flask_restful import Resource
from flask import jsonify, request
from helper import verify_pw, count_tokens
from db_String import users


class Get(Resource):
    def post(self):
        posted_data = request.get_json()

        user_name = posted_data["user_name"]
        password = posted_data["password"]

        correct_pw = verify_pw(user_name, password)

        if not correct_pw:
            return_json = {
                "status": 302
            }
            return jsonify(return_json)

        num_tokens = count_tokens(user_name)
        if num_tokens <= 0:
            return_json = {
                "status": 301
            }
            return jsonify(return_json)

        sentence = users.find({
            "user_name": user_name
        })[0]["Sentence"]

        return_json = {
            "status": 200,
            "sentence": sentence
        }
