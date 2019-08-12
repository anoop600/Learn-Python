from flask import request
from flask_restful import Resource
from db_string import users
from helper import generate_return_dictionary, verify_credentials, cash_with_user, update_account


class Add(Resource):
    def post(self):
        posted_data = request.get_json()
        user_name = posted_data["user_name"]
        password = posted_data["password"]
        money = posted_data["amount"]
        return_json, error = verify_credentials(user_name, password)

        if error:
            return return_json

        if money <= 0:
            return generate_return_dictionary(304, "Money amount enteered must be  > 0")

        cash = cash_with_user(user_name)
        money -= 1
        bank_cash = cash_with_user("BANK")
        update_account("BANK", bank_cash+1)
        update_account(user_name, cash+money)

        return generate_return_dictionary(200, "Amount added successfully to Account")
