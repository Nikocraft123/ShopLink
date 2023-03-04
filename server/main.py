from flask import Flask, render_template
import api


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

    app.run(debug=True, port=80, threaded=True)
