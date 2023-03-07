from flask import Flask, render_template


app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404


import api
import doc

app.register_blueprint(api.bp, url_prefix="/api/")
app.register_blueprint(doc.bp, url_prefix="/doc/")


def run():

    print("Start flask server")

    app.run(debug=True, use_reloader=False, port=80, threaded=True)

    print("Flask server exited")
