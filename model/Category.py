from manage import db, _get_date_time

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Enum('A', 'D', 'C'), nullable=False)
    bill = db.relationship('Bill', backref='category', lazy=True)
