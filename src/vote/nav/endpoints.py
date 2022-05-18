from flask import Blueprint, render_template
from vote.general.decorators import connexion_requise
from vote.models.categorie import Categorie
from vote.models.utilisateur import Utilisateur
from vote.models.vote import Vote
from vote.nav.business import data_par_cat

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
    return render_template("index.html", data=data)

