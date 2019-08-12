from flask import Flask
from flask_restful import Api
from Register import Register
from Add import Add
from Transfer import Transfer
from Take_Loan import TakeLoan
from Pay_Loan import PayLoan
from Balance import Balance
app = Flask(__name__)
api = Api(app)


api.add_resource(Register, "/register")
api.add_resource(Add, "/add")
api.add_resource(Transfer, "/transfer")
api.add_resource(Balance, "/balance")
api.add_resource(TakeLoan, "/takeloan")
api.add_resource(PayLoan, "/payloan")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
