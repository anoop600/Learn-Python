from flask import Flask
from flask_restful import Api, Resource
from add import Add
from subtract import Subtract
from multiply import Multiply
from divide import Divide
from pymongo import MongoClient

# Initialize FLASK app
app = Flask(__name__)
# Initialize RestFul API for the flask App
api = Api(app)
client = MongoClient("mongodb://db:27017")

db = client.aNewDB
user_num = db["user_num"]

user_num.insert_one({
    'count': 0
})


class Visit(Resource):
    def get(self):
        prev_num = user_num.find({})[0]['count']
        new_num = prev_num + 1
        user_num.update_one({}, {"$set": {"count": new_num}})
        return str("hello user " + str(new_num))


# REST-API-Controller
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")
api.add_resource(Visit, "/hello")


@app.route('/')
def hello_world():
    return "Simple Calculator !"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
