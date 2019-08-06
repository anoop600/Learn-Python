from pymongo import MongoClient
from flask_restful import Resource

client = MongoClient("mongodb://db:27017")

db = client.aNewDB
user_num = db["user_num"]

user_num.insert({
    'count': 0
})


class Visit(Resource):
    def get(self):
        prev_num = user_num.find({})[0]['count']
        new_num = prev_num + 1
        user_num.update({}, {"$set": {"count": new_num}})
        return str("hello user " + str(new_num))
