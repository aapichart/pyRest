""" Flask configuration """
from os import environ, path
from dotenv import load_dotenv
import datetime

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.flaskenv'))

class Config:
    """ Set Flask config variable """
    FLASK_ENV = 'development'
    TESTING = True
    # Using for authentication between sever tier
    SECRET_KEY = environ.get('SECRET_KEY') 
    # Using TOKEN_TIMEOUT for setting token life (in minutes) after login
    TOKEN_TIMEOUT = 480
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    # Using these data for contact webapi
    WEB_API_IP = environ.get('WEB_API_IP')
    WEB_API_PORT = environ.get('WEB_API_PORT')

    # for jwt configuration
    JWT_SECRET_KEY = environ.get("SECRET_KEY", 'local-secret')
    JWT_TOKEN_LOCATION = ['headers','cookies']
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=1800)
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    JWT_SESSION_COOKIE = False 
    JWT_COOKIE_SECURE = False
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=15)
    JWT_COOKIE_CSRF_PROTECT = True 
    JWT_COOKIE_SAMESITE = 'lax'
    JWT_ACCESS_CSRF_HEADER_NAME = "X-CSRF-TOKEN-ACCESS"
    JWT_REFRESH_CSRF_HEADER_NAME = "X-CSRF-TOKEN-REFRESH"   
    # CORS setup
    CORS_HEADERS = 'Content-Type'
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

