
from flask import Blueprint, render_template
from vote.votes.business import candidat

votes_bp = Blueprint('votes_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/votes'
)

@votes_bp.route('/')
def vote():
    return render_template("vote.html", content=candidat)