from run import db


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Enum('A', 'D', 'C'), nullable=False)

    # bills = db.relationship('Bill', backref='category', lazy=True)

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def save_to_bd(self):
        db.session.add(self)
        db.session.commit()

    def update_to_bd(self):
        db.session.merge(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_type(cls, type):
        return cls.query.filter_by(type=type).all()

    def json(self):
        return {'id': self.id, 'name': self.name, 'type': self.type}
