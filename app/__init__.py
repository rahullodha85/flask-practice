import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    db.init_app(application)
    migrate = Migrate(application, db)
    from app.user import models
    return application


config_name = os.getenv('ENV')
app = create_app(config_name)
