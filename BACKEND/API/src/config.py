from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True  # Turn on debugging features in Flask


config = {
    'development': DevelopmentConfig,
}
