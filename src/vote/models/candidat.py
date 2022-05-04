"""
    définition de la classe Candidat SQLAlchemy
    (interface vers la table candidat)
"""
from vote import db

class Candidat(db.Model):
    """Modèle candidat pour la base de données"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    classe = db.Column(db.String(2), nullable=False)
    genre = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        me = f"<Candidat id={self.id} prenom={self.prenom}, nom={self.nom},"
        me += f" classe={self.classe}, genre={self.genre}>" 
        return me
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    