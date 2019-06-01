class Config(object):
    """
    Default configurations
    """
    SECRET_KEY = 'my_secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    """
    Local dev config
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test123@localhost:3306/flask-practice'


class ProdConfig(Config):
    """
    production config
    """


app_config = {
    'dev': DevConfig,
    'prod': ProdConfig
}
