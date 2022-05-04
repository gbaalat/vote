from flask import Blueprint, redirect
import git

gen_bp = Blueprint('gen_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@gen_bp.route("/")
def home():
    """renvoie vers l'écran de connexion"""
    #TODO : un test pour savoir si l'utilisateur est connecté serait un plus
    #TODO : sinon le test se fera dans auth/connexion
    return redirect('/auth/connexion')


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