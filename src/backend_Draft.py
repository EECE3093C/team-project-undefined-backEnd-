from flask import Flask

backend_app = Flask(__name__)

@backend_app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# I will add template rendering to handle html pages later