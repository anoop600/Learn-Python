from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from db_string import users
from register import Register
from helper import user_exist
import bcrypt
import requests
import subprocess
import json

app = Flask(__name__)
api = Api(app)

def verify_pw(user_name,password):
    if not user_exist(user_name):
        return False
    hashed_pw = users.find({
        "user_name": user_name
    })[0]["passsword"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw)==hashed_pw:
        return True
    else:
        return True

def generateReturnDictionary(status,msg):
    return_json = {
        "status": status,
        "msg": msg
    }
    return jsonify(return_json)

def verifyCredentials(user_name,password):
    if not user_exist(user_name):
        return generateReturnDictionary(301,"Invalid Username"), True
    correct_pw = verify_pw(user_name,password)
    if not correct_pw:
        return generateReturnDictionary(302, "Invalid Password"), True
    return None, False



class Classify(Resource):
    def post(self):
        posted_data = request.get_json()
        user_name = posted_data["user_name"]
        password = posted_data["password"]
        ur = posted_data["url"]

        return_json ,error = verifyCredentials(user_name,password)
        if error:
            return jsonify(return_json)

        tokens = users.find({
            "user_name": user_name
        })[0]["token"]

        if tokens <=0:
            return jsonify(generateReturnDictionary(303,"Not Enough Tokens ! "))

        r = requests.get(url)
        return_json = {}
        with open("temp.jpg","web") as f:
            f.write(r.content)
            proc = subprocess.Popen('python classify_image.py --model_dir=. --image_file=./temp.jpg')
            proc.communicate()[0]
            proc.wait()
            with open("text.txt") as g:
                return_json = json.load(g)

            users.update({
                "user_name": user_name
            },{
                "$set": tokens-1
            })
        return return_json

api.add_resource(Register, "/register")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
