from flask import jsonify, request
from db_string import users
from helper import user_exist, verify_password, count_tokens
from flask_restful import Resource
import spacy


class Detect(Resource):
    def post(self):
        posted_data = request.get_json()
        user_name = posted_data["user_name"]
        password = posted_data["password"]
        text1 = posted_data["text1"]
        text2 = posted_data["text2"]

        if not user_exist(user_name):
            return_json = {
                "status": 301,
                "msg": "Invalid Username"
            }
            return jsonify(return_json)

        correct_pw = verify_password(user_name, password)

        if not correct_pw:
            return_json = {
                "status": 302,
                "msg": "invalid Password"
            }

            return jsonify(return_json)

        num_tokens = count_tokens(user_name)

        if num_tokens <= 0:
            return_json = {
                "status": 303,
                "msg": "You are out of tokens"
            }
            return jsonify(return_json)

        nlp = spacy.load('en_core_web_sm')

        text1 = nlp(text1)
        text2 = nlp(text2)

        ratio = text1.similarity(text2)

        return_json = {
            "status": 200,
            "similarity": ratio,
            "msg": "Similarity score calculated"
        }

        current_tokens = count_tokens(user_name)

        users.update({
            "user_name": user_name
        }, {
            "$set": {
                "token": current_tokens - 1
            }
        })

        return jsonify(return_json)
