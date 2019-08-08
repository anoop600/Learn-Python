from flask_restful import Resource
from flask import request,jsonify
from db_string import users
from helper import verifyCredentials,generateReturnDictionary
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
        print("\n\n\n\n\n\n"+tokens+"\n\n\n\n\n")
        if tokens <=0:
            return jsonify(generateReturnDictionary(303,"Not Enough Tokens ! "))

        r = requests.get(ur)
        return_json = {}
        with open("temp.jpg","wb") as f:
            f.write(r.content)
            proc = subprocess.Popen("python classify_image.py --model_dir=. --image_file=temp.jpg",shell=True)
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