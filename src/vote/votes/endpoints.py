from flask import Blueprint, redirect, render_template, request, session, url_for
from vote.votes.business import (
    obtenirCandidats,
    obtenirCategorie,
    dico,
    jeVote,
    categoriesVotees,
)
from vote.general.decorators import connexion_requise

votes_bp = Blueprint(
    "votes_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/votes",
)


@votes_bp.route("/<int:categorie_id>", methods=["GET", "POST"])
@connexion_requise
def vote(categorie_id):
    cate = obtenirCategorie(categorie_id)
    if cate.ouvert == True:
        if request.method == "GET":
            listeCatVotees = categoriesVotees(session["id"])
            if categorie_id in listeCatVotees:
                return render_template("mauvaisVote.html")
            else:
                return render_template(
                    "vote.html",
                    content=obtenirCandidats(categorie_id),
                    cat=obtenirCategorie(categorie_id),
                    dico=dico,
                )
        elif request.method == "POST":
            idCandidat = request.form["idCandidat"]
            jeVote(categorie_id, idCandidat, session["id"])
            return redirect(url_for("nav_bp.nav"))
    else:
        return redirect(url_for("nav_bp.nav"))
