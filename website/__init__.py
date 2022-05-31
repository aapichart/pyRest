from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('ENV_SETTING')
    app.config.from_object('config.DevConfig')

    #  create route for application
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
