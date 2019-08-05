from helper import check_posted_data,return_data
from flask import request
from flask_restful import Resource
class Divide(Resource):
    def post(self):
        # If I am here, then the resource Add was requested using the method POST

        # Step 1 : Get posted data
        posted_data = request.get_json()
        # Step 2 : Check if data is in proper format
        print("calling checkPostde data")
        status_code = check_posted_data(posted_data, "divide")
        print("Status Code : "+str(status_code))
        if(status_code != 200):
            if(status_code == 302):
                print("Inside 302")
                return return_data(status_code, "Divide by Zero Exception")
            else:
                print("Inside 301")
                return return_data(status_code, "An error happened")
        # Process the data
        x = posted_data["x"]
        y = posted_data["y"]

        x = int(x)
        y = int(y)
        ret = x/y
        # Retun the result
        return return_data(status_code, ret)