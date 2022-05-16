from functools import wraps
from flask import session, flash, redirect, url_for

def connexion_requise(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not 'id' in session:
            flash("Accès refusé : merci de vous identifier")
            return redirect(url_for("auth_bp.connexion"))
        else:
            setattr(decorated, 'id', session['id'])
        return f(*args, **kwargs)
    return decorated