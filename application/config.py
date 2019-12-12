class BaseConfig(object):
    ORIGINS = ["*"]
    SECRET_KEY = '4)-.W\xad\x80\x97`\x8e\xc1\xcd\x10\xd7\x11\xd6\x00\xf7M\x89\x18\xceCg'
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
