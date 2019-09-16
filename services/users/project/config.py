# services/users/project/config.py

class BaseConfig:
    """ Base configuration"""
    TESTING = False

class DevelopmentConfig:
    """ Development Config """
    pass

class TestingConfig:
    """Testing config"""
    TESTING = True

class ProductionConfig:
    """Production config"""
    pass
