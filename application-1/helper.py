from flask import jsonify


def return_data(status_code, message):
    return_json = {
        'Message': message,
        'Status Code': status_code
    }
    # retun
    return jsonify(return_json)


def check_present_in_posted_data(posted_data):
    return "x" not in posted_data or "y" not in posted_data


def validate_for_divide(posted_data):
    if check_present_in_posted_data(posted_data) == True:
        return 301
    elif int(posted_data["y"]) == 0:
        return 302
    else:
        return 200


def validate_for_other(posted_data):
    if check_present_in_posted_data(posted_data) == True:
        return 301  # missing parameter
    else:
        return 200  # All OK


def validate_posted_data_type(posted_data):
    return isinstance(posted_data["x"], int) and isinstance(posted_data["y"], int)


def check_posted_data(posted_data, method):
    if validate_posted_data_type(posted_data) == True:
        if (method == "divide"):
            return validate_for_divide(posted_data)
        if (method == "add" or method == "subtract" or method == "multiply"):
            return validate_for_other(posted_data)
    else:
        return 303  # Type mismatch required int
