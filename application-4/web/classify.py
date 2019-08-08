from flask_restful import Resource
from flask import request,jsonify
from helper import verifyCredentials, generateReturnDictionary
from db_string import users
import requests
import subprocess
import json

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

        r = requests.get(ur)
        return_json = {}
        with open("temp.jpg","wb") as f:
            f.write(r.content)
            proc = subprocess.Popen('python classfy_image.py --model_dir=. --image_file=./temp.jpg')
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