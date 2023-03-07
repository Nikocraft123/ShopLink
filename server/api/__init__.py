from flask import Blueprint


UNKNOWN = 1
MISSING_VERSION = 2
INVALID_VERSION = 3
USING_GET = 4


bp = Blueprint("api", __name__)


from . import v1


@bp.post("/")
def missing_version():
    return {"exit_code": MISSING_VERSION, "error_message": "Missing version! Example: /api/v1/"}


@bp.post("/<path:ver>/")
def invalid_version(ver):
    return {"exit_code": INVALID_VERSION, "error_message": "Invalid version! Example: /api/v1/"}


@bp.get("/", defaults={"path": ""})
@bp.get("/<path:path>/")
def using_get(path):
    return {"exit_code": USING_GET, "error_message": "Invalid method! Please use POST!"}


bp.register_blueprint(v1.api, url_prefix="/v1/")
