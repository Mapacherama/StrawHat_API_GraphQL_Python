from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os

from api.routes import *
from api.models import *

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_ENGINE = os.environ.get("DATABASE_ENGINE")
SERVER_NAME = os.environ.get("SERVER_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_ENGINE + DATABASE_USER + ":" + DATABASE_PASSWORD + DATABASE_URL + DATABASE_NAME
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#test

from api.routes import *
from api.models import *

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

