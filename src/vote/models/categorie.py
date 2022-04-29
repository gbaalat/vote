"""
    définition de la classe Categorie SQLAlchemy
    (interface vers la table categorie)
"""
from vote import db

class Categorie(db.Model):
    """Modèle categorie pour la base de données"""

    niveau = db.Column(db.String(1), primary_key=True)
    genre = db.Column(db.String(1), primary_key=True)

    def __repr__(self):
        return (
            f"<Categorie niveau={self.niveau}, genre={self.genre}>"
        )
