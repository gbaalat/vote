"""
    Flask CLI : accès depuis la ligne de commande
    
    Les modèles SQLAlchemy (comme Utilisateur) doivent être importés
    dans ce fichier pour être détectés par Flask-Migrate
"""
import os

from vote import create_app, db
from vote.models.utilisateur import Utilisateur
from vote.models.candidat import Candidat
from vote.models.categorie import Categorie
from vote.models.vote import Vote

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Utilisateur": Utilisateur,
        "Candidat": Candidat,
        "Categorie": Categorie,
        "Vote": Vote
    }

