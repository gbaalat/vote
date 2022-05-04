from click import pass_context
from flask import Blueprint, render_template

votes_bp = Blueprint('votes_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/votes'
)

@votes_bp.route('/')
def vote():
    pass