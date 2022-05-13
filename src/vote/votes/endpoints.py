
from flask import Blueprint, render_template, request, session
from vote.votes.business import obtenirCandidats, obtenirCategorie, dico

votes_bp = Blueprint('votes_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/votes'
)

@votes_bp.route('/<int:categorie_id>', methods=['GET', 'POST'])
def vote(categorie_id):
    if request.method == 'GET':
        return render_template("vote.html", content=obtenirCandidats(categorie_id), cat = obtenirCategorie(categorie_id), dico = dico)
    elif request.method == 'POST':
        idCandidat = request.form["idCandidat"] 
        vote(categorie_id, idCandidat, session["id"])