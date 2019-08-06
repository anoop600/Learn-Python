from flask import Flask
from flask_restful import Api
from add import Add
from subtract import Subtract
from multiply import Multiply
from divide import Divide
from visit_count import Visit

# Initialize FLASK app
app = Flask(__name__)
# Initialize RestFul API for the flask App
api = Api(app)


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