""" Flask configuration """
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.flaskenv'))

class Config:
    """ Set Flask config variable """
    FLASK_ENV = 'development'
    TESTING = True
    # Using for authentication between sever tier
    SECRET_KEY = 'Pamelo'
    # Using TOKEN_TIMEOUT for setting token life (in minutes) after login
    TOKEN_TIMEOUT = 480
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # for Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True 
    TESTING = True 
    # for Database
    DATABASE_URI = environ.get('DEV_DATABASE_URI')

