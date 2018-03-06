# Install

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
# add .env
``
DATABASE_URL="mysql://root:root@localhost/flask_skeleton"
APP_SETTINGS="config.StagingConfig"
``
```
$ export DATABASE_URL="mysql://root:root@localhost/flask_skeleton"
$ export APP_SETTINGS="config.StagingConfig"
```
# Manager / Migrate
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
```
