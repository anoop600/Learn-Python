from flask import jsonify
def return_data(status_code, message):
    return_json = {
        'Message': message,
        'Status Code': status_code
    }
    # retun
    return jsonify(return_json)


def check_posted_data(posted_data, method):
    if(isinstance(posted_data["x"],int) and isinstance(posted_data["y"],int)):
        if (method == "divide"):
            
            if "x" not in posted_data or "y" not in posted_data:
                return 301
            elif int(posted_data["y"]) == 0:
                return 302
            else:
                return 200
        if(method == "add" or method == "subtract" or method == "multiply"):
            if "x" not in posted_data or "y" not in posted_data:
                return 301  # missing parameter
            else:
                return 200  # All OK
    else:
        return 303 #Type mismatch required int