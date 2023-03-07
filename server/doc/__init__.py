from flask import Blueprint, render_template


bp = Blueprint("doc", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("doc.html")


@bp.route("/<path:ver>/", methods=["GET", "POST"])
def invalid_version(ver):
    return render_template("error.html")
