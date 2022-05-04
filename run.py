"""
    Flask CLI : accès depuis la ligne de commande
    
    Les modèles SQLAlchemy (comme Utilisateur) doivent être importés
    dans ce fichier pour être détectés par Flask-Migrate
"""
import os

from vote import create_app, db, mail
from vote.models.utilisateur import Utilisateur

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Utilisateur": Utilisateur
    }

