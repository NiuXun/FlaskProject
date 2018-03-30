import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 基类
class Config(object):
    DEBUG = True
    # SECRET_KEY = 'this is secret_key'
    SECRET_KEY = 'a4439d4b-d9fd-4c55-ba09-97453d6a09f3'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:P@ssw0rd@127.0.0.1:3306/OAMP'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


config = {
    'default': Config,
}
