from flask import Blueprint
import git

auth_bp = Blueprint(
    "gen_bp", __name__, template_folder="templates", static_folder="static"
)


@auth_bp.route("/git_update", methods=["POST"])
def git_update():
    repo = git.Repo("./vote")
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(
        origin.refs.main
    ).checkout()
    origin.pull()
    return "", 200
