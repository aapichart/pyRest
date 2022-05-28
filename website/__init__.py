from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('ENV_SETTING')

    os.environ['PG_USER'] = app.config.get('PG_USER')
    os.environ['PG_PASSWD'] = app.config.get('PG_PASSWD')
    os.environ['PG_HOST'] = app.config.get('PG_HOST')
    os.environ['PG_PORT'] = app.config.get('PG_PORT')
    os.environ['PG_DBNAME'] = app.config.get('PG_DBNAME')

    db.init_app(app)
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
