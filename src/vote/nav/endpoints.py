from flask import Blueprint, redirect, render_template, request, session, url_for
from vote.general.decorators import connexion_requise
from vote.models.categorie import Categorie
from vote.models.utilisateur import Utilisateur
from vote.models.vote import Vote
from vote.nav.business import data_par_cat
from vote import db

nav_bp = Blueprint(
    "nav_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/nav",
)


@nav_bp.route("/")
@connexion_requise
def nav():        
    data = data_par_cat(nav.id)
    admin=Utilisateur.query.filter(Utilisateur.id==session["id"]).first().admin
    return render_template("index.html", data=data, admin=admin)


@nav_bp.route("/activeCategorie/<int:categorie_id>")
def activeCategorie(categorie_id):
    a=Categorie.query.filter(Categorie.id==categorie_id).first()
    a.swap_ouverture()
    db.session.add(a)
    db.session.commit()
    return redirect(url_for("nav_bp.nav"))
    