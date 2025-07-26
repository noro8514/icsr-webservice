import os
from dotenv import load_dotenv
from flask import Flask, request, abort, render_template
from flask_cors import CORS

import sentry_sdk

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "ICSR Test Route"

if __name__ == '__main__':
    app.run()