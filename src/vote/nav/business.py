from sqlalchemy import and_, func
from vote import db
from vote.models.candidat import Candidat
from vote.models.categorie import Categorie
from vote.models.vote import Vote

def top3(genre, niveau):
    q = (
        db.session.query(Candidat.id, Candidat.nom, Candidat.prenom, func.count(Vote.id))
        .select_from(Candidat)
        .join(Vote, Vote.id_candidat == Candidat.id)
        .join(Categorie, Categorie.id == Vote.id_categorie)
        .filter(and_(Categorie.genre == genre, Categorie.niveau == niveau))
        .group_by(Candidat.id)
        .order_by(func.count().desc())
    )
    classement = q.all()
    max = len(classement)
    podium = {}
    i = 0
    if i < max and classement[0][3] >= 3:
        podium[1] = [classement[0]]
        i += 1
        while i < max and classement[i][3] == classement[i-1][3]:
            podium[1].append(classement[i])
            i += 1
        # gestion 2ème place(s)
        if i < max and i <= 3:
            podium[2] = [classement[i]]
            i += 1
            while i < max and classement[i][3] == classement[i-1][3]:
                podium[2].append(classement[i])
                i += 1
        # gestion 3ème place(s)
        if i < max and i <= 3:
            podium[3] = [classement[i]]
            i += 1
            while i < max and classement[i][3] == classement[i-1][3]:
                podium[3].append(classement[i])
                i += 1
    return podium

def categoriesVotees(id_utilisateur):
    
    ssReq = (
        db.session.query(Categorie.id)
        .select_from(Categorie)
        .join(Vote, Vote.id_categorie == Categorie.id)
        .filter(Vote.id_user == id_utilisateur)
        .subquery()
    )
    q = (
        db.session.query(Categorie.id, Categorie.genre, Categorie.niveau, Categorie.ouvert, ssReq.c.id)
        .select_from(Categorie)
        .outerjoin(ssReq, Categorie.id == ssReq.c.id)
    )
    return q

def label_cat(genre, niveau):
    if niveau == "S":
        return "Garçon seconde" if genre == "M" else "Fille seconde"
    elif niveau == "P":
        return "Garçon première" if genre == "M" else "Fille première"
    else:
        return "Garçon terminale" if genre == "M" else "Fille terminale"


def data_par_cat(id_utilisateur):
    data = []
    for tup in categoriesVotees(id_utilisateur).all():
        cat = {"id": tup[0], "nom": label_cat(tup[1], tup[2]), "ouvert": tup[3], "aVote": bool(tup[4])}
        cat["top3"] = top3(tup[1], tup[2])
        data.append(cat)
    return data
