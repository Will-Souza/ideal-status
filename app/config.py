class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'lalala'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    DB_NAME = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''

    IMAGE_UPLOADS = ''

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    DB_NAME = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''

    IMAGE_UPLOADS = ''

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    DB_NAME = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''

    SESSION_COOKIE_SECURE = False