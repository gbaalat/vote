"""
    définition de la classe Candidat SQLAlchemy
    (interface vers la table candidat)
"""
from vote import db
from vote.models.vote import Vote
from sqlalchemy import func


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

    def compte_vote(self):
        """
        SELECT count(utilisateur.id)
        FROM vote
        JOIN utilisateur AS vote.id_user = utilisateur.id
        WHERE id_candidat = {candidat}

        u = candidat.query.select_from("vote")
        u = candidat.query.join("vote", "candidat.id" == "vote.id_candidat")
        u = candidat.query.filter("vote.id_candidat" == candidat)
        """

        nb_vote = (Vote.query.filter(Vote.id_candidat == self.id)).count()
        return nb_vote

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
