from os import environ as env

class BaseConfig(object):
    ORIGINS = ["*"]
    SECRET_KEY = env['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLIMATEMPO_TOKEN = "b22460a8b91ac5f1d48f5b7029891b53"


class Development(BaseConfig):
    PORT = 5000
    DEBUG = True
    TESTING = True
    ENV = 'dev'
    APP_NAME = "WeatherPrediction"


class Production(BaseConfig):
    PORT = 8080
    DEBUG = False
    TESTING = False
    ENV = 'production'
    APP_NAME = "WeatherPrediction"
