from flask_sqlalchemy import SQLAlchemy
import datetime
from app import app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def _get_date_time():
    return datetime.datetime.now()
