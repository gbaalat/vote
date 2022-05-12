from vote.models.categorie import Categorie
from vote.models.candidat import Candidat

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
    liste = Candidat.query.filter(Candidat.genre == genre, Candidat.classe.like("%" + classe + "%")).all()
    candidats = []
    for eleve in liste:
        provisoire = {'nom': eleve.nom,'prénom' : eleve.prenom, 'classe': eleve.classe }
        candidats.append(provisoire)
    return candidats

def obtenirCategorie(idCategorie):
    nomCategorie = ""
    cat = Categorie.query.get(idCategorie)
    if cat.genre == "M":
        nomCategorie = "Garçons "
    if cat.genre == "F":
        nomCategorie = "Filles "
    if cat.niveau == "T" :
        nomCategorie += "Terminale"
    if cat.niveau == "P" :
        nomCategorie += "Première"
    if cat.niveau == "S" :
        nomCategorie += "Seconde"
    return nomCategorie
   