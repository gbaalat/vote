from flask import flash, url_for, redirect, session
from vote.models.utilisateur import Utilisateur

def validation(email, mdp):
        if not(email and mdp) or len(mdp)<8:
            flash("Entrez des valeurs valides")
            return redirect(url_for('auth_bp.connexion'))
        else:
            email = email.strip()   #enlève les espaces superflus
            mdp = mdp.strip()
    
        u = Utilisateur.query.filter_by(email=email).first()

        if not(u.verify_email(email)) or not(u.verify_mdp(email, mdp)):
            flash("Email ou mot de passe incorrect, veuillez réessayer")
            return redirect(url_for('auth_bp.connexion'))
        else:
            session['id'] = u.id
            return redirect(url_for("nav_bp.nav"))