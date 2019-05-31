class Config(object):
    """
    Default configurations
    """
    SECRET_KEY = 'my_secret'


class DevConfig(Config):
    """
    Local dev config
    """
    DEBUG = True


class ProdConfig(Config):
    """
    production config
    """


app_config = {
    'dev': DevConfig,
    'prod': ProdConfig
}
