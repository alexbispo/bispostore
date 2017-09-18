# Create user and database on Postgres
$ sudo -i -u postgres

$ psql

postgres=# create user bispo_store_app with createdb login password 'dev123';

postgres=# create database bispostore_db owner = bispo_store_app encoding = 'UTF-8'

# Create a Python virtualenv
$ sudo apt-get install python-virtualenv

$ cd $PROJECT_HOME/

$ virtualenv venv -p python3.5

$ source venv/bin/activate

# Install Django
$ pip install django

# Create a Django project
$ django-admin startproject my_project

# Create a django app super user
## Development
$ ./manage.py createsuperuser

...

## Production (heroku)
$ heroku run manage.py createsuperuser

...

# Deploy
$ git push heroku master

...

$ heroku run python manage.py migrate

...
