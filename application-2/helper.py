from db_String import users
import bcrypt


def verify_pw(user_name, password):
    hashed_pw = users.find({
        "UserName": user_name
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def count_tokens(user_name):
    tokens = users.find({
        "UserName": user_name
    })[0]["Tokens"]
    return tokens
