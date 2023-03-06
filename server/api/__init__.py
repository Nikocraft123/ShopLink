from flask import Blueprint

UNKNOWN = 1
MISSING_VERSION = 2
INVALID_VERSION = 3

bp = Blueprint("api", __name__)

from . import v1


@bp.route("/", methods=["GET", "POST"])
def missing_version():
    return {"exit_code": MISSING_VERSION, "error_message": "Missing version! Example: /api/v1/"}


@bp.route("/<path:ver>/", methods=["GET", "POST"])
def invalid_version(ver):
    return {"exit_code": INVALID_VERSION, "error_message": "Invalid version! Example: /api/v1/"}


bp.register_blueprint(v1.api, url_prefix="/v1/")
