from run import db, _get_date_time


class TagModel(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, name, active):
        self.name = name
        self.active = active

    def json(self):
        return {'id': self.id, 'name': self.name, 'active': self.active}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
