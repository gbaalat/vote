"""
    fixtures pour pytest
    https://pytest-flask.readthedocs.io/en/latest/features.html
"""
import pytest

from vote import create_app
from vote import db as database
from vote.models.utilisateur import Utilisateur


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture
def db(app, client, request):
    database.drop_all()
    database.create_all()
    database.session.commit()

    def fin():
        database.session.remove()

    request.addfinalizer(fin)
    return database
