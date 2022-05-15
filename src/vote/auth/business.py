from flask import flash, redirect, session, url_for
from vote.models.utilisateur import Utilisateur
from vote.__init__ import mail
from flask_mail import Message 
from vote import db

def validation(email, mdp):
    u = Utilisateur.query.filter_by(email=email).first()
    if u is None or not(u.verify_email(email) and u.verify_mdp(email, mdp)):
        flash("Email ou mot de passe incorrect, veuillez réessayer")
        return redirect(url_for('auth_bp.connexion'))
    else:
        session['id'] = u.id
        return redirect(url_for("nav_bp.nav"))

def creer_utilisateur(adresse_mail):
    u=Utilisateur(email=adresse_mail)
    db.session.add(u)
    db.session.commit()
    u=Utilisateur.query.filter(Utilisateur.email==adresse_mail).first()
    return u.public_id
    
def envoi_mail(html,recipient):
	msg = Message("Sujet du mail",recipients=[recipient])
	msg.html=html
	mail.send(msg)

def test_utilisateur(adresse_mail):
    if Utilisateur.query.filter(Utilisateur.email == adresse_mail).first()==None:
        return True 
    else:
        return 
