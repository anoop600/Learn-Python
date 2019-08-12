from db_string import users
from flask import Flask, jsonify
import bcrypt


def user_exist(user_name):
    if users.find({"user_name": user_name}).count() == 0:
        return False
    else:
        return True


def verify_password(user_name, password):
    if not user_exist(user_name):
        return False

    hashd_pw = users.find({
        "user_name": user_name
    })[0]["password"]
    if bcrypt.hashpw(password.encode('utf8'), hashd_pw) == hashd_pw:
        return True
    else:
        return False


def debt_with_user(user_name):
    debt = users.find({
        "user_name": user_name
    })[0]["debt"]
    return debt


def cash_with_user(user_name):
    cash = users.find({
        "user_name": user_name
    })[0]["own"]
    return cash


def generate_return_dictionary(status, msg):
    return_json = {
        "status": status,
        "msg": msg
    }
    return jsonify(return_json)


def verify_credentials(user_name, password):
    if not user_exist(user_name):
        return generate_return_dictionary(301, "Invalid username"), True
    correct_pw = verify_password(user_name, password)

    if not correct_pw:
        return generate_return_dictionary(302, "Incorrect Password"), True

    return None, False


def update_account(user_name, balance):
    users.update({
        "user_name": user_name
    }, {
        "$set": {
            "own": balance
        }
    })


def update_debt(user_name, balance):
    users.update({
        "user_name": user_name
    }, {
        "$set": {
            "debt": balance
        }
    })
