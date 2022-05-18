from flask import Blueprint, redirect, render_template, request, flash, url_for, session
from vote.models.utilisateur import Utilisateur
from vote.auth.business import creer_utilisateur, envoi_mail, test_utilisateur

auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/auth'
)


@auth_bp.route('/inscription', methods=["GET", "POST"])
def inscription():
    """Page d'insciption, l'utilisateur y rentre son adresse mail, envoi du mail quand la méthode est POST"""
    if request.method == "POST":
        if test_utilisateur(request.form["email"]):
            public_id=creer_utilisateur(request.form["email"])
            envoi_mail(render_template("mail.html",public_id=public_id),request.form["email"])
        else:
            flash("Adresse mail déjà utilisée")
    return render_template("auth_inscription.html")

@auth_bp.route('/creerMdp/<string:public_id>', methods=["GET", "POST"])
def creerMdp(public_id):
    """Page dont le lien est contenu dans le mail d'inscription afin de définir le mot de passe du nouveau compte."""
    if request.method == "POST":
        if Utilisateur.enregistrerMdp(public_id, request.form["mdp"]):
            return redirect(url_for("auth_bp.connexion"))
        else:
            flash("Utilisateur introuvable, le mot de passe a peut-être déjà été changé.")
    return render_template("auth_creerMdp.html", public_id = public_id)

@auth_bp.route('/connexion', methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        email = request.form['email']
        mdp = request.form['mdp']
        email, mdp = email.strip(), mdp.strip()   #enlève les espaces superflus
        u = Utilisateur.query.filter_by(email=email).first()
        if u is None or not(u.verify_email(email) and u.verify_mdp(email, mdp)):
            flash("Email ou mot de passe incorrect, veuillez réessayer")
            return redirect(url_for('auth_bp.connexion'))
        else:
            session['id'] = u.id
            return redirect(url_for("nav_bp.nav"))
    return render_template("auth_connexion.html")

@auth_bp.route('/deconnexion')
def deconnexion():
    session.pop('id')
    flash('Vous vous êtes bien déconnecté(e)')
    return redirect(url_for('auth_bp.connexion'))

@auth_bp.route('/motDePasseOublie')
def motDePasseOublie():
    if request.method == "POST":
        email = request.form["email"].strip()
        u = Utilisateur.query.filter_by(email=email).first()
        if u is None or not(u.verify_email(email)):
            flash("Email incorrect, veuillez réessayer")
            return redirect(url_for('auth_bp.motDePasseOublie'))
        else:
            mdp = u.mdp
            envoi_mail(render_template("mail.html",mdp=mdp),email) #recuperer mail.html et diriger vers un autre template (contenu du mail)
            flash("Mail envoyé !")
    return render_template("auth_oubli_mdp.html")

@auth_bp.route('/changerMotDePasse')
def changerMotDePasse():
    pass
