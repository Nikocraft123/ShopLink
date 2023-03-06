print("Initialize")

from flask import Flask, render_template
import api
import os

import database


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/doc/", methods=["GET", "POST"])
def doc():
    return render_template("doc.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404


app.register_blueprint(api.bp, url_prefix="/api/")


if __name__ == '__main__':

    try:
        with open("./secret.key", "rb") as f:
            app.secret_key = f.read()
    except OSError:
        app.secret_key = os.urandom(24)
        with open("./secret.key", "wb") as f:
            f.write(app.secret_key)

    database.init()

    print("Run")

    app.run(debug=True, use_reloader=False, port=80, threaded=True)

    print("Exit")

    database.close()
