from flask import Blueprint, render_template
from vote.models.categorie import Categorie
from vote.models.vote import Vote

nav_bp = Blueprint(
    "nav_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/nav",
)


@nav_bp.route("/")
def nav():
    categories = Categorie.query.all()
    return render_template("index.html", categories=categories, Vote = Vote)
