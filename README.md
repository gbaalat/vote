# vote

vote en ligne : projet de terminale NSI à l'Immaculée Conception de Pau

## installation en mode développement

### mise à jour du système
`sudo apt update`
`sudo apt upgrade`

### récupérer un token github

voir avec le propriétaire du github

### installation github CLI

1. suivre les [commandes d'installation](https://github.com/cli/cli/blob/trunk/docs/install_linuxmd#debian-ubuntu-linux-raspberry-pi-os-apt)

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
Maj des outils de packaging:
* `pip install --upgrade pip setuptools wheel`

### config git
* `git init`
* `git config user.name mon_nom`
* `git config user.email mon_email`

### installation du projet

`pip install -e .[dev]`

## Outils

* setuptools Right gestion de l’installation et autres tâches liées info
utile dès que l’application a d’autres dépendances que la librairie standard python.
* venv Right environnement virtuel pour python info
utilité : conserver les logiciels (dépendances notamment) et leur version (version
python par exemple) dans un environnement séparé de l’OS
En cas de mise à jour, l’environnement de développement n’est pas modifié.

## Dépendences
* **Pytest** : framework facilitant l’écriture de tests → info
* **python-dotenv** → ce package permet à notre application de changer la configuration
automatiquement (variables d’environnement) à partir d’un fichier .env
* **Black** code formatter → info
black file ou black repo modifie en place les fichiers python en imposant un style
uniforme (espaces, commentaires, sauts de ligne etc...) → cf codeStyle
* **Flake8** linter (outil d’analyse statique du code)→ info
l’outil signale des erreurs / warnings pour des bugs potentiels, constructions suspectes
etc....
* **Flask-SQLAlchemy** ORM pour Flask
* **Flask-Migrate**
Au fil du développement, la base de données peut avoir besoin d’évoluer
Après modification des classes SQLAlchemy (représentant les tables), cet outil
permettra la migration de la base de données sous-jacente.

## fichiers de Config
* **.env** → ce fichier ne doit pas être envoyé à l’hébergeur (via git par exemple)
FLASK_APP=run.py chemin vers l’application info
FLASK_ENV=development active le debugger automatiquement info
SECRET_KEY="à modifier" pour la signature crypto info
* **config.py**
configuration développement/tests/production pour notre application
* **pyproject.toml** → fichier de configuration
utilisé ici pour Black (code formatter)

on peut modifier :
- line-length : nombre de caractères autorisés sur une ligne de code
- target-version : version python
- include / exclude : expressions régulières déterminant les fichiers à formater
* **pytest.ini** → configuration du framework de test pytest
* **setup.py** → configuration pour setuptools exemple documenté

## Autre fichiers
* **README.md** file → info
permet de présenter le projet avec un guide d’installation, de la documentation etc.
* **.gitignore** liste les fichiers / dossiers qui ne seront pas pris en compte par le gestionnaire de
versions (git) et ne seront donc pas hébergés → exemple
* **__init__.py** → info et package_vs_module
principe en python :
- on met des fonctions dans un fichier .py appelé module
- on met des modules dans un dossier appelé package
\__init__.py permet de marquer le dossier dans lequel il se trouve comme un package
il est exécuté à chaque import d’un module de ce package
\__init__.py peut être vide (juste présent comme marqueur de package) ou contenir du
code d’initialisation (chargement de la config, connexion à la base de données etc ...)