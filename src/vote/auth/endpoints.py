from flask import Blueprint, redirect, render_template, request, flash, url_for, session
from vote.models.utilisateur import Utilisateur
from vote.auth.business import creer_utilisateur, envoi_mail, test_utilisateur

auth_bp = Blueprint(
    "auth_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/auth",
)


@auth_bp.route("/inscription", methods=["GET", "POST"])
def inscription():
    """Page d'insciption, l'utilisateur y rentre son adresse mail, envoi du mail quand la méthode est POST"""
    if request.method == "POST":
        email=str(request.form["email"])
        if test_utilisateur(email):
            public_id = creer_utilisateur(email)
            envoi_mail(
                render_template("mail.html", public_id=public_id), email
            )
            flash(f"Un mail a été envoyé à cette adresse : {email}")
        else:
            flash("Adresse mail déjà utilisée")
    if "id" in session:
        return redirect(url_for("nav_bp.nav")),flash("Déconnectez-vous pour vous inscrire.")
    else:
        return render_template("auth_inscription.html")


@auth_bp.route("/creerMdp/<string:public_id>", methods=["GET", "POST"])
def creerMdp(public_id):
    """Page dont le lien est contenu dans le mail d'inscription afin de définir le mot de passe du nouveau compte."""
    public_id = str(public_id) # Validation de base
    if request.method == "POST":
        if Utilisateur.enregistrerMdp(public_id, str(request.form["mdp"])):
            return redirect(url_for("auth_bp.connexion"))
        else:
            flash(
                "Utilisateur introuvable, le mot de passe a peut-être déjà été changé."
            )
    return render_template("auth_creerMdp.html", public_id=public_id)


@auth_bp.route("/connexion", methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        email = str(request.form["email"])
        mdp = str(request.form["mdp"])
        email, mdp = email.strip(), mdp.strip()  # enlève les espaces superflus
        u = Utilisateur.query.filter_by(email=email).first()
        if u is None or not (u.verify_email(email) and u.verify_mdp(email, mdp)):
            flash("Email ou mot de passe incorrect, veuillez réessayer")
            return redirect(url_for("auth_bp.connexion"))
        else:
            session["id"] = u.id
            return redirect(url_for("nav_bp.nav"))
    if "id" in session:
        flash("Déconnectez-vous pour vous connecter à un autre compte.")
        return redirect(url_for("nav_bp.nav"))
    else:
        return render_template("auth_connexion.html")


@auth_bp.route("/deconnexion")
def deconnexion():
    session.pop("id")
    flash("Vous vous êtes bien déconnecté(e)")
    return redirect(url_for("auth_bp.connexion"))


@auth_bp.route("/motDePasseOublie", methods=["GET", "POST"])
def motDePasseOublie():
    if request.method == "POST":
        email = str(request.form["email"])
        email = email.strip()
        u = Utilisateur.query.filter_by(email=email).first()
        if u is None or not(u.verify_email(email)):
            flash("Email incorrect, veuillez réessayer")
            return redirect(url_for('auth_bp.motDePasseOublie'))
        else:
            public_id = u.public_id
            envoi_mail(
                render_template("mail_oubli_mdp.html", public_id = public_id), email
            )
            flash(f"Un mail a été envoyé à cette adresse : {email}")
    return render_template("auth_oubli_mdp.html")


@auth_bp.route("/changerMotDePasse")
def changerMotDePasse():
    pass
