import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bookinfo", methods=["POST"])
def bookinfo():

    # Query for book
    book = request.form.get("book")
    res = requests.get("https://www.googleapis.com/books/v1/volumes", params={"q": book})

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})

    data = res.json()
    return jsonify({"success": True, "items": data["items"]})