import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'secret key'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    CONFIG_NAME = 'Development'

    ENV = 'development'

    DEBUG = True
    TESTING = True


class GitlabConfig(DevelopmentConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'gitlab': GitlabConfig,
    'default': DevelopmentConfig
}
