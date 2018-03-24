import os, datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    JWT_AUTH_URL_RULE = '/login'
    JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=1800)
    JWT_AUTH_USERNAME_KEY = 'email'

class ProductionConfig(Config):
    DEBUG = False
    BUNDLE_ERRORS = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    BUNDLE_ERRORS = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    BUNDLE_ERRORS = True


class TestingConfig(Config):
    TESTING = True
