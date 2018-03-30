from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import config

# 实例化
db = SQLAlchemy()
csrf = CSRFProtect()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 初始化
    config[config_name].init_app(app)
    csrf.init_app(app)
    db.init_app(app)

    # 注册home
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    # 注册users
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')

    # 注册assets
    from .assets import assets as assets_blueprint
    app.register_blueprint(assets_blueprint, url_prefix='/assets')

    return app
