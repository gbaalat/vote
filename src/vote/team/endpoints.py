from flask import Blueprint, render_template


team_bp = Blueprint(
    "team_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/team",
)


@team_bp.route("/")
def team():
    return render_template("team.html")
