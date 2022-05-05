from flask import Blueprint, render_template

nav_bp = Blueprint('nav_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/nav'
)

@nav_bp.route('/<categories>')
def nav(categories):
    return render_template("index.html")

