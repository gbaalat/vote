from flask import Blueprint, render_template, request, flash
from vote.auth.business import creer_utilisateur, envoi_mail, test_utilisateur

auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)


@auth_bp.route('/inscription', methods=["GET", "POST"])
def inscription():
    """Page d'insciption, l'utilisateur y rentre son adresse mail, envoi du mail quand la méthode est POST"""
    if request.method == "POST":
        if test_utilisateur(request.form["email"]):
            public_id=creer_utilisateur(request.form["email"])
            envoi_mail(render_template("mail.html",public_id=public_id),request.form["email"])
        else:
            flash("Adresse mail déjà utilisée")
    return render_template("auth_inscription.html")

@auth_bp.route('/creerCompte')
def creerCompte():
    """Page dont le lien est contenu dans le mail d'inscription."""
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
