import os
from flask import Flask
app = Flask(__name__)


@app.route("/hello")
def hello():
    foo = os.environ.get('FOO')
    return f'Hello World! Env Value: {foo}'
