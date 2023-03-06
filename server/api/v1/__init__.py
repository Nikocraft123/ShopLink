from flask import Blueprint, request
import json

from .error import *

api = Blueprint("v1", __name__)


def decode() -> tuple[bool, dict]:

    if request.method == "GET":
        return False, {"exit_code": USING_GET, "error_message": "Cannot use GET! Please use POST!"}

    try:
        data = json.loads(request.data.decode("utf-8"))
    except UnicodeError:
        return False, {"exit_code": NO_UTF8, "error_message": "Invalid encoding! Please use UTF-8!"}
    except json.JSONDecodeError:
        return False, {"exit_code": NO_JSON, "error_message": "Invalid JSON!"}

    return True, data


from . import auth


@api.route("/", methods=["GET", "POST"])
def missing_function():
    return {"exit_code": MISSING_FUNCTION, "error_message": "Missing function! Example: /api/v1/login/"}


@api.route("/<path:func>/", methods=["GET", "POST"])
def invalid_function(func):
    return {"exit_code": INVALID_FUNCTION, "error_message": "Invalid function! Example: /api/v1/login/"}
