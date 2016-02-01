import os
from flask import Flask, url_for
from flask_mail import Mail
from datetime import date
from pymongo import MongoClient
from . import config

app = Flask(__name__)
APP_NAME = 'pryvacy'

app.config.from_object('%s.config.Develop' % APP_NAME)

# Database
if os.environ.get('HEROKU'):
    uri = os.environ.get('MONGOLAB_URI')
    db = MongoClient(host=uri).get_default_database()
else:
    db = MongoClient()[APP_NAME]

mail = Mail(app)

# register routes
from . import routes


# Template Globals
app.jinja_env.globals['year'] = date.today().year
