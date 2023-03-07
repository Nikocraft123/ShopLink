from flask import Blueprint, request
import json


api = Blueprint("v1", __name__)


from .error import *


def decode() -> tuple[bool, dict]:

    try:
        data = json.loads(request.data.decode("utf-8"))
    except UnicodeError:
        return False, {"exit_code": NO_UTF8, "error_message": "Invalid encoding! Please use UTF-8!"}
    except json.JSONDecodeError:
        return False, {"exit_code": NO_JSON, "error_message": "Invalid JSON!"}

    return True, data


from . import auth


@api.post("/")
def missing_function():
    return {"exit_code": MISSING_FUNCTION, "error_message": "Missing function! Example: /api/v1/login/"}


@api.post("/<path:func>/")
def invalid_function(func):
    return {"exit_code": INVALID_FUNCTION, "error_message": "Invalid function! Example: /api/v1/login/"}
