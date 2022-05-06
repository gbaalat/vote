
from flask import Blueprint, render_template
from vote.votes.business import obtenirCandidats

votes_bp = Blueprint('votes_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/votes'
)

@votes_bp.route('/<int:categorie_id>')
def vote(categorie_id):
    
    return render_template("vote.html", content=obtenirCandidats(categorie_id))