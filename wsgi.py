from flask import Flask
from flask import jsonify

application = Flask(__name__)


json_data = {
    "username": "admin",
    "email": "admin@localhost",
    "id": 42
}

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/health")
def health():
    return "OK"

@application.route("/limited-endpoint")
def limit():
    return "limited endpoint"

@application.route("/ping")
def ping():
    return "pong"


@application.route("/json-test")
def json_test():
    return jsonify(
        {
            "username": "admin",
            "email": "admin@localhost",
            "id": 42
        }
    )

if __name__ == "__main__":
    application.run()
