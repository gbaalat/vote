"""
    définition de la classe Vote SQLAlchemy
    (interface vers la table vote)
"""
from vote import db

#Continuer à modifier

class Vote(db.Model):
    """Modèle vote pour la base de données"""

    id_user = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), primary_key=True)
    id_candidat = db.Column(db.Integer, db.ForeignKey("candidat.id"), nullable=False)
    categorie = db.Column(db.String(2), db.ForeignKey("categorie.id"), primary_key=True)

    def __repr__(self):
        return (
            f"<Vote votant={self.id_user}, candidat={self.id_candidat}, categorie={self.categorie}>"
        )
    
    