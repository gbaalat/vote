from flask import Blueprint, redirect, session, url_for
import git

gen_bp = Blueprint('gen_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/gen'
)


@gen_bp.route("/")
def home():
    """renvoie vers l'écran d'accueil"""
    return redirect(url_for("nav_bp.nav"))



@gen_bp.route("/git_update", methods=["POST"])
def git_update():
    """
    fonction pour l'intégration continue
    le hook github envoie un HTTP POST sur voteICBF.pythonanywhere.com/git_update
    """
    repo = git.Repo("./vote")
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(
        origin.refs.main
    ).checkout()
    origin.pull()
    return "", 200