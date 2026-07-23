from flask import Flask, request, abort

app = Flask(__name__)

SECRET_PASSWORD = "password123"


@app.route("/")
def home():
    return "This is the public page."


@app.route("/secret")
def secret_page():
    password = request.args.get("password")

    if password == SECRET_PASSWORD:
        return "This is the secret page!"
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
