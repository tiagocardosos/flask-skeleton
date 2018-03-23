import datetime
import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['BUNDLE_ERRORS'] = True
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

