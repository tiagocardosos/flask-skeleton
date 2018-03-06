import datetime

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

def _get_date_time():
    return datetime.datetime.now()
