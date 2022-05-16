from flask import flash, redirect, session, url_for
from vote.models.utilisateur import Utilisateur
from vote.__init__ import mail
from flask_mail import Message
from vote import db


def creer_utilisateur(adresse_mail):
    u = Utilisateur(email=adresse_mail)
    db.session.add(u)
    db.session.commit()
    u = Utilisateur.query.filter(Utilisateur.email == adresse_mail).first()
    return u.public_id


def envoi_mail(html, recipient):
    msg = Message("Sujet du mail", recipients=[recipient])
    msg.html = html
    mail.send(msg)


def test_utilisateur(adresse_mail):
    if Utilisateur.query.filter(Utilisateur.email == adresse_mail).first() == None:
        return True
    else:
        return
