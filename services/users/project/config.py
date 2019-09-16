# services/users/project/config.py
import os

class BaseConfig:
    """ Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig:
    """ Development Config """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig:
    """Testing config"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig:
    """Production config"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
