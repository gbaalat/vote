# vote

vote en ligne : projet de terminale NSI à l'Immaculée Conception de Pau

## AVANT DE DEVELOPPER 

 * ouvrir un terminal et se placer à la racine du projet avec `cd`
 * lancer l'environnement virtuel `source venv/bin/activate`
 * ouvrir l'IDE avec `code .`

## modification de la base de donnée

 la création de la base se fait via `flask db init` 

 Ensuite:
 * créer le script sql de migration avec `flask db migrate --message "ajout du modèle candidat"`
 * lancer la migration avec `flask db upgrade`
 Ces deux points sont à relancer à chaque modification des classes modèles (src/vote/models/...)

Le script d'insertion des candidats est dans le dossier script à la racine du projet ainsi que la commande sqlite à lancer (chemins à modifier)

## installation en mode développement

### mise à jour du système
`sudo apt update`  
`sudo apt upgrade`

### récupérer un token github

voir avec le propriétaire du github

### installation github CLI

1. suivre les [commandes d'installation](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)

2. `gh auth login` et suivre les instructions, ie sélectionner:
    * github
    * HTTPS
    * store credentials
    * puis coller votre token

### récupérer le projet

* `git clone https://github.com/gbaalat/vote.git`
* se déplacer dans le dossier créé avec `cd`


### créer l'environnement virtuel

* `python3 -m venv venv --prompt vote`  pour le créer
* `source venv/bin/activate` pour l'activer
* `pip install --upgrade pip setuptools wheel` maj des outils de packaging

### config git
* `git init`
* `git config user.name mon_nom`
* `git config user.email mon_email`

### installation du projet

`pip install -e .[dev]`

## Outils

 * **setuptools** -> gestion de l’installation et autres tâches liées [info](https://en.wikipedia.org/wiki/Setuptools)  
utile dès que l’application a d’autres dépendances que la [librairie standard python](https://docs.python.org/3/library/index.html)
 * **venv** -> environnement virtuel pour python [info](https://docs.python.org/3/library/venv.html)  
utilité : conserver les logiciels (dépendances notamment) et leur version (version python par exemple) dans un environnement séparé de l’OS  
En cas de mise à jour, l’environnement de développement n’est pas modifié.

## Dépendences
 * **Pytest** -> framework facilitant l’écriture de tests  [info](https://docs.pytest.org/en/7.1.x/)
 * **python-dotenv** -> ce package permet à notre application de changer la configuration
automatiquement (variables d’environnement) à partir d’un fichier .env
 * **Black** (code formatter) -> [info](https://github.com/psf/black)
black file ou black repo modifie en place les fichiers python en imposant un style
uniforme (espaces, commentaires, sauts de ligne etc...) → cf [codeStyle](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
* **Flake8** (linter, i.e. outil d’analyse statique du code) -> [info](https://flake8.pycqa.org/en/latest/user/index.html)
l’outil signale des erreurs / warnings pour des bugs potentiels, constructions suspectes etc....
* **Flask-SQLAlchemy** ORM pour Flask
* **Flask-Migrate** -> Au fil du développement, la base de données peut avoir besoin d’évoluer  
Après modification des classes SQLAlchemy (représentant les tables), cet outil permettra la migration de la base de données sous-jacente.

## fichiers de Config
* **.env** -> ce fichier ne doit pas être envoyé à l’hébergeur (via git par exemple)
FLASK_APP=run.py chemin vers l’application [info](https://flask.palletsprojects.com/en/1.0.x/cli/#application-discovery)
FLASK_ENV=development active le debugger automatiquement [info](https://flask.palletsprojects.com/en/1.0.x/config/#environment-and-debug-features)
SECRET_KEY="à modifier" pour la signature crypto [info](https://flask.palletsprojects.com/en/1.0.x/config/#SECRET_KEY)
* **config.py** -> configuration développement/tests/production pour notre application
* **pyproject.toml** -> fichier de configuration
utilisé ici pour Black (code formatter)
on peut modifier :
     - line-length : nombre de caractères autorisés sur une ligne de code
     - target-version : version python
     - include / exclude : expressions régulières déterminant les fichiers à formater
* **pytest.ini** -> configuration du framework de test pytest
* **setup.py** -> configuration pour setuptools [exemple documenté](https://github.com/pypa/sampleproject/blob/main/setup.py)
* **.gitignore** -> liste les fichiers / dossiers qui ne seront pas pris en compte par le gestionnaire de
versions (git) et ne seront donc pas hébergés → [exemple](https://github.com/github/gitignore/blob/main/Python.gitignore)

## Autre fichiers
* **README.md** -> le présent fichier markdown [readme](https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f)
permet de présenter le projet avec un guide d’installation, de la documentation etc.
* **__init__.py** -> [info](https://docs.python.org/3/reference/import.html#regular-packages) et [package_vs_module](https://pythongeeks.org/python-modules-vs-packages/)  
principe en python :
    - on met des fonctions dans un fichier .py appelé module
    - on met des modules dans un dossier appelé package  
\__init__.py permet de marquer le dossier dans lequel il se trouve comme un package  
il est exécuté à chaque import d’un module de ce package  
\__init__.py peut être vide (juste présent comme marqueur de package) ou contenir du
code d’initialisation (chargement de la config, connexion à la base de données etc ...)
