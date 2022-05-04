"""
    définition de la classe Vote SQLAlchemy
    (interface vers la table vote)
"""
from vote import db
from sqlalchemy import ForeignKeyConstraint

class Vote(db.Model):
    """Modèle vote pour la base de données"""
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), primary_key=True)
    id_candidat = db.Column(db.Integer, db.ForeignKey("candidat.id"), nullable=False)
    categorie = db.Column(db.Integer, db.ForeignKey("categorie.id"), primary_key=True)
    
    user = db.relationship("Utilisateur", db.backref("vote"))
    candidat = db.relationship("Candidat", db.backref("vote"))
    cate = db.relationship("Categorie", db.backref("vote"))

    def __repr__(self):
        return (
            f"<Vote votant={self.id_user}, candidat={self.id_candidat}, categorie={self.categorie}>"
        )
    
    