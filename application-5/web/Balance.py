from flask import request, jsonify
from flask_restful import Resource
from helper import verify_credentials
from db_string import users


class Balance(Resource):
    def post(self):
        posted_data = request.get_json()
        user_name = posted_data["user_name"]
        password = posted_data["password"]

        return_json, error = verify_credentials(user_name, password)
        if error:
            return return_json

        return_json = users.find({
            "user_name": user_name
        }, {
            "password": 0,
            "_id": 0
        })[0]
        return jsonify(return_json)
