# Flask APIs
This code base serves as starting point for writing your next Flask application.

# Install
Clone this repo, set up and activate a virtualenv and install the required python dependencies
```
git clone https://github.com/tiagocardosos/flask-skeleton
cd flask-skeleton
virtualenv VENV
source VENV/bin/activate
pip install -r requirements.txt

export DATABASE_URL="mysql://root:root@localhost/flask_skeleton"
export APP_SETTINGS="config.StagingConfig"
```
# Create file .env
```
DATABASE_URL="mysql://root:root@localhost/flask_skeleton"
APP_SETTINGS="config.StagingConfig"
```
# Manager / Migrate
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
```

# Fakers
# Logging

# Run
```
$ python run.py
```

# Register
``
curl localhost:5000/register -d '{"name": "teste", "email": "email@email.com", "password": 123321}' -H 'Content-Type: application/json'
``
# Login
``
curl localhost:5000/login -d '{"email":"email@email.com", "password": "123321"}' -H 'Content-Type: application/json'
``

# Logged
``
curl -X GET \
  http://localhost:5000/logged \
  -H 'authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjE4MzU3OTUsImlhdCI6MTUyMTgzMzk5NSwibmJmIjoxNTIxODMzOTk1LCJpZGVudGl0eSI6NH0.RS0VuxJH7Gs7LDircp5As_85ZE2mzEKWgqEbATP4sPs' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json'
``

#Acknowledgements
With thanks to the following Flask extensions:

- Alembic
- Flask
- Flask-Migrate
- Flask-Script
- Flask-JWT
- Flask-RESTful
- Flask-SQLAlchemy

#Authors
- Tiago Cardoso -- tiagocardosos AT gmail DOT com