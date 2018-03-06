from run import db, _get_date_time

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('bill_id', db.Integer, db.ForeignKey('bills.id'), primary_key=True))

class Bill(db.Model):
    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    total = db.Column(db.DECIMAL(13, 2))
    status = db.Column(db.Enum('O', 'C', 'F'), server_default='O', nullable=False)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('bills', lazy=True))

