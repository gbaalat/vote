from flask import flash
from vote.models.categorie import Categorie
from vote.models.candidat import Candidat
from vote.models.utilisateur import Utilisateur
from vote.models.vote import Vote
from vote import db

"""
a = {'nom':'Rimbaud', 'prénom' : 'Arthur', 'classe': 'T°2'}
b = {'nom':'Dufaud', 'prénom' : 'Bertrand', 'classe': 'T°3'}
c = {'nom':'Brava', 'prénom' : 'Caroline', 'classe': 'T°2'}
d = {'nom':'Brava', 'prénom' : 'Carla', 'classe': 'T°1'}
candidat = a, b, c, d
"""


def obtenirCandidats(idCategorie):
    genre = Categorie.query.get(idCategorie).genre
    classe = Categorie.query.get(idCategorie).niveau[0]
    liste = Candidat.query.filter(
        Candidat.genre == genre, Candidat.classe.like("%" + classe + "%")
    ).all()
    candidats = []
    for eleve in liste:
        provisoire = {
            "nom": eleve.nom,
            "prénom": eleve.prenom,
            "classe": eleve.classe,
            "identifiant": eleve.id,
        }
        candidats.append(provisoire)
    return candidats


dico = {"M": "Garçons", "F": "Filles", "T": "Terminale", "P": "Première", "S": "Seconde"}


def obtenirCategorie(idCategorie):
    cat = Categorie.query.get(idCategorie)
    return cat


def jeVote(idCategorie, idCandidat, idUser):
    v = Vote(id_user=idUser, id_candidat=idCandidat, id_categorie=idCategorie)
    db.session.add(v)
    db.session.commit()
    flash("A voté")


def categoriesVotees(idUser):
    liste = Vote.query.filter(Vote.id_user == idUser).all()
    catVotees = []
    for cat in liste:
        catVotees.append(cat.id_categorie)
    return catVotees
