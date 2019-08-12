from flask import request
from flask_restful import Resource
from helper import verify_credentials, cash_with_user, generate_return_dictionary, debt_with_user, update_account, update_debt


class Pay_Loan(Resource):
    def post(self):
        posted_data = request.get_json()
        user_name = posted_data["user_name"]
        password = posted_data["password"]
        money = posted_data["amount"]
        return_json, error = verify_credentials(user_name, password)
        if error:
            return return_json
        cash = cash_with_user(user_name)
        if cash < money:
            return generate_return_dictionary(303, "Not enough cash in your account")
        debt = debt_with_user(user_name)
        update_account(user_name, cash-money)
        update_debt(user_name, debt-money)
        return generate_return_dictionary(200, "successfully pain loan")
