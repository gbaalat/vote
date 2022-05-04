from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)

@auth_bp.route('/')
def auth():
    pass

@auth_bp.route('/adresseMail')
def adresseMail():
    return render_template("auth_inscription.html")

@auth_bp.route('/envoyerMail')
def envoyerMail():
    pass

@auth_bp.route('/creerCompte')
def creerCompte():
    pass

@auth_bp.route('/connexion')
def connexion():
    return render_template("auth_connexion.html")

@auth_bp.route('/motDePasseOublie')
def motDePasseOublie():
    pass

@auth_bp.route('/changerMotDePasse')
def changerMotDePasse():
    pass
