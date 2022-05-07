from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'xxxxxx'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://apichart:chartx.123@10.135.70.133:49159'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app
