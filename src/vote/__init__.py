"""initialisation de Flask (factory pattern)"""
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

from vote.config import get_config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app(config_name):
    app = Flask("vote")
    app.config.from_object(get_config(config_name))

    from vote.auth.endpoints import auth_bp
    from vote.nav.endpoints import nav_bp
    from vote.votes.endpoints import votes_bp
    from vote.general.endpoints import gen_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(nav_bp)
    app.register_blueprint(votes_bp)
    app.register_blueprint(gen_bp)
    
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    return app
