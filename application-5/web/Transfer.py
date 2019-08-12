from flask_restful import Resource
from flask import request
from helper import verify_credentials, cash_with_user, generate_return_dictionary, user_exist, update_account


class Transfer(Resource):
    def post(self):
        posted_data = request.get_json()
        user_name = posted_data["user_name"]
        password = posted_data["password"]
        to = posted_data["to"]
        money = posted_data["amount"]

        return_json, error = verify_credentials(user_name, password)
        if error:
            return return_json
        cash = cash_with_user(user_name)
        if cash <= 0:
            return generate_return_dictionary(304, "Out of money, please add or take loan")

        if not user_exist(to):
            return generate_return_dictionary(301, "Reciever username is invalid")
        cash_from = cash_with_user(user_name)
        cash_to = cash_with_user(to)
        bank_cash = cash_with_user("BANK")
        update_account("BANK", bank_cash+1)
        update_account(to, cash_to+money - 1)
        update_account(user_name, cash_from-money)
        return generate_return_dictionary(200, "Amount Transfered Successfully")
