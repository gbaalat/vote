from flask import Blueprint, render_template

auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)

@auth_bp.route('/')
def login():
    return render_template('auth/login.html')