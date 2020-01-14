from flask import Flask
from flask import jsonify

application = Flask(__name__)


json_data = {
    "username": "admin",
    "email": "admin@localhost",
    "id": 42
}

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@application.route('/400')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)



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
