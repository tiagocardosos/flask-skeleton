from database import db, _get_date_time
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    remember_token = db.Column(db.String(60))
    created_at = db.Column(db.DateTime(), default=_get_date_time)
    updated_at = db.Column(db.DateTime(), onupdate=_get_date_time)
    deleted_at = db.Column(db.DateTime())
    # bills = db.relationship('Bill', backref='users', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save_to_bd(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def json(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

