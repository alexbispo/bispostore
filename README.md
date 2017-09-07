# Create user and database on Postgres
$ sudo -i -u postgres

postgres$ create user my_user with createdb login password 'my_password';

# Create a Python virtualenv
$ sudo apt-get install python-virtualenv

$ cd $PROJECT_HOME/

$ virtualenv venv -p python3.5

$ source venv/bin/activate

# Install Django
$ pip install django

# Create a Django project
$ django-admin startproject my_project