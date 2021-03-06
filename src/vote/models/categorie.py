"""
    définition de la classe Categorie SQLAlchemy
    (interface vers la table categorie)
"""
from vote import db


class Categorie(db.Model):
    """Modèle categorie pour la base de données"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    niveau = db.Column(db.String(1), nullable=False)
    genre = db.Column(db.String(1), nullable=False)
    ouvert = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Categorie id={self.id} niveau={self.niveau}, genre={self.genre}>"
    
    def swap_ouverture(self):
        if self.ouvert:
            self.ouvert = False
        else:
            self.ouvert = True

