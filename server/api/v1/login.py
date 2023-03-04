from flask import request
import json

from . import api
from .error import *


@api.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return {"exit_code": USING_GET, "error_message": "Cannot use GET! Please use POST!"}

    try:
        data = json.loads(request.data.decode("utf-8"))
    except UnicodeError:
        return {"exit_code": NO_UTF8, "error_message": "Invalid encoding! Please use UTF-8!"}
    except json.JSONDecodeError:
        return {"exit_code": NO_JSON, "error_message": "Invalid JSON!"}

    if "username" not in data:
        return {"exit_code": MISSING_USERNAME, "error_message": "Missing username field!"}
    if "password" not in data:
        return {"exit_code": MISSING_PASSWORD, "error_message": "Missing password field!"}

    print(data["username"], data["password"])

    return {"exit_code": 0}
