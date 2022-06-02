from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def webapi_link_app(app):

    from .users_route import users_web_api 
    from .auth_route import auth_web_api
    from .coupon_route import coupon_web_api

    db.init_app(app)
    
    app.register_blueprint(users_web_api, url_prefix='/api')
    app.register_blueprint(auth_web_api, url_prefix='/api')
    app.register_blueprint(coupon_web_api, url_prefix='/api')
    
    return app

