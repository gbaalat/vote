from flask import Blueprint, render_template, request, session, flash, url_for, redirect
from vote.auth.business import validation
from vote.models.utilisateur import Utilisateur

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
        email, mdp = email.strip(), mdp.strip()   #enlève les espaces superflus
        
        u = Utilisateur.query.filter_by(email=email).first()

        if u is None or not(u.verify_email(email) and u.verify_mdp(email, mdp)):
            flash("Email ou mot de passe incorrect, veuillez réessayer")
            return redirect(url_for('auth_bp.connexion'))
        else:
            session['id'] = u.id
            return redirect(url_for("nav_bp.nav"))
    return render_template("auth_connexion.html")

@auth_bp.route('/motDePasseOublie')
def motDePasseOublie():
    pass

@auth_bp.route('/changerMotDePasse')
def changerMotDePasse():
    pass
