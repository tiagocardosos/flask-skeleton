import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# from marshmallow_sqlalchemy import ModelSchema
from model import User, Bill, Tag, Category

from app import app
from database import db

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def db_fresh():
    db.drop_all()
    db.create_all()


@manager.command
def db_drop():
    db.drop_all()


if __name__ == '__main__':
    manager.run()
