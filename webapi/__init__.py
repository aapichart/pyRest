from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

def link_app(app):
    from .users import users
    app.register_blueprint(users, url_prefix='/')
    return app

