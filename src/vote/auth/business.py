from flask import flash, redirect, session, url_for
from vote.models.utilisateur import Utilisateur

def validation(email, mdp):
    u = Utilisateur.query.filter_by(email=email).first()
    if u is None or not(u.verify_email(email) and u.verify_mdp(email, mdp)):
        flash("Email ou mot de passe incorrect, veuillez réessayer")
        return redirect(url_for('auth_bp.connexion'))
    else:
        session['id'] = u.id
        return redirect(url_for("nav_bp.nav"))

def enregistrerMdp(publicKey, mdp):
    pass
