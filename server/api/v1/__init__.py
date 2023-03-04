from flask import Blueprint

from .error import *

api = Blueprint("v1", __name__)

from . import login


@api.route("/", methods=["GET", "POST"])
def missing_function():
    return {"exit_code": MISSING_FUNCTION, "error_message": "Missing function! Example: /api/v1/login/"}


@api.route("/<path:func>/", methods=["GET", "POST"])
def invalid_function(func):
    return {"exit_code": INVALID_FUNCTION, "error_message": "Invalid function! Example: /api/v1/login/"}
