from manage import db
from manage import _get_date_time


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    remember_token = db.Column(db.String(60))
    created_at = db.Column(db.DateTime(), server_default=_get_date_time)
    updated_at = db.Column(db.DateTime(), onupdate=_get_date_time)
    deleted_at = db.Column(db.DateTime())
    bills = db.relationship('Bill', backref='user', lazy=True)
