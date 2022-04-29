"""initialisation de Flask (factory pattern)"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from vote.config import get_config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask("vote")
    app.config.from_object(get_config(config_name))

    from vote.auth.endpoints import auth_bp
    app.register_blueprint(auth_bp)
    
    db.init_app(app)
    migrate.init_app(app, db)
    return app
