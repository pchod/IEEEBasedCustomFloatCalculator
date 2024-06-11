import os

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")


@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/hello")
def hello_api():
    return {"message": "Hello from Flask!"}
