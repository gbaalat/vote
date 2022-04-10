"""tests de l'environnement et de la config associée"""
import os

from vote import create_app
from vote.config import SQLITE_DEV, SQLITE_PROD, SQLITE_TEST


def test_config_development():
    app = create_app("development")
    assert app.config["SECRET_KEY"] != "open me"
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_URL", SQLITE_DEV)


def test_config_testing():
    app = create_app("testing")
    assert app.config["SECRET_KEY"] != "open me"
    assert app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == SQLITE_TEST


def test_config_production():
    app = create_app("production")
    assert app.config["SECRET_KEY"] != "open me"
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv(
        "DATABASE_URL", SQLITE_PROD
    )
