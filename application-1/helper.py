from flask import jsonify


def return_data(status_code, message):
    return_json = {
        'Message': message,
        'Status Code': status_code
    }
    # retun
    return jsonify(return_json)


def validate_posted_data_type(posted_data):
    return isinstance(posted_data["x"], int) and isinstance(posted_data["y"], int)
	
def validate_for_divide(posted_data):
    if int(posted_data["y"]) == 0:
        return 302
    else:
        return 200

def check_posted_data(posted_data, method):
	if "x" not in posted_data or "y" not in posted_data:
		return 301
	if validate_posted_data_type(posted_data):
        if (method == "divide"):
			return validate_for_divide(posted_data)
		elif(method == "add" or method == "subtract" or method == "multiply"):
			return 200
	else:
        return 303 #Type mismatch required int