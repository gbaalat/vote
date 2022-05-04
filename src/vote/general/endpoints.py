from click import pass_context
from flask import Blueprint, render_template

gen_bp = Blueprint('gen_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


