from db_string import users
import bcrypt

def user_exist(user_name):
    if users.find({"user_name": user_name}).count() == 0:
        return False
    else:
        return True


def verifyPw(user_name, password):
    if not user_exist(user_name):
        return False
    hashed_pw = users.find({
        "user_name": user_name
    })[0]["password"]

    if bcrypt.hashed_pw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def count_tokens(user_name):
    tokens = users.find({
        "user_name": user_name
    })[0]["token"]
    return tokens
