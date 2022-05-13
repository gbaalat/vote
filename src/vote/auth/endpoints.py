from flask import Blueprint, render_template, request
from vote.auth.business import validation

auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)


@auth_bp.route('/inscription', methods=["GET", "POST"])
def inscription():
    """Page d'insciption, l'utilisateur y rentre son adresse mail, envoi du mail quand la méthode est POST"""
    if request.method == "POST":
        pass
    return render_template("auth_inscription.html")

@auth_bp.route('/creerCompte')
def creerCompte():
    """Page dont le lien est contenu dans le mail d'inscription."""
    pass

@auth_bp.route('/connexion', methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        email = request.form['email']
        mdp = request.form['mdp']
        validation(email, mdp)
    return render_template("auth_connexion.html")

@auth_bp.route('/motDePasseOublie')
def motDePasseOublie():
    pass

@auth_bp.route('/changerMotDePasse')
def changerMotDePasse():
    pass
