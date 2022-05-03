"""Configuration pour les environnements de dev, de test et de production"""
import os
from pathlib import Path


HERE = Path(__file__).parent
SQLITE_DEV = "sqlite:///" + str(HERE / "vote_dev.db")
SQLITE_TEST = "sqlite:///" + str(HERE / "vote_test.db")
SQLITE_PROD = "sqlite:///" + str(HERE / "vote_prod.db")


class Config:
    """configuration par défaut"""

    SECRET_KEY = os.getenv("SECRET_KEY", "open me")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "aspmx.l.google.com"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = False
    MAIL_PASSWORD = False


    MAIL_DEBUG = True
    MAIL_SUPPRESS_SEND = False

    MAIL_DEFAULT_SENDER = ("Sender","test@gmail.com")
    MAIL_MAX_EMAILS = None
    MAIL_ASCII_ATTACHMENTS = False
    

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQLITE_TEST


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_DEV)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_PROD)
    PRESERVE_CONTEXT_ON_EXCEPTION = True


ENV_CONFIG_DICT = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config(config_name):
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
