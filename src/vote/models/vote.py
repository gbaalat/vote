"""
    définition de la classe Vote SQLAlchemy
    (interface vers la table vote)
"""
from vote import db


class Vote(db.Model):
    """Modèle vote pour la base de données"""
    __table_args__ = (db.UniqueConstraint('id_user', 'id_categorie'),)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), nullable=False)
    id_candidat = db.Column(db.Integer, db.ForeignKey("candidat.id"), nullable=False)
    id_categorie = db.Column(db.Integer, db.ForeignKey("categorie.id"), nullable=False)
    vote_possible = db.Column(db.Boolean, default=True)

    # user = db.relationship("Utilisateur", db.backref("vote"))
    # candidat = db.relationship("Candidat", db.backref("vote"))
    # cate = db.relationship("Categorie", db.backref("vote"))

    def __repr__(self):
        me = f"<Vote id={self.id} votant={self.id_user}, candidat={self.id_candidat},"
        me += f" categorie={self.id_categorie}>"
        return me
