"""script d'installation"""
from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = "Outil de vote en ligne au lycée Immaculée Conception de Pau"
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Mainguy Côme, Labrouche Ilona, Hourdebaight Yan, Lescoulié Maël, Degos Arnaud"
PROJECT_URLS = {
    "Documentation": "https://...",
    "Source Code": "https://....",
}
INSTALL_REQUIRES = [
    "Flask",
    "Flask-Migrate",
    "Flask-SQLAlchemy",
    "Flask-Mail",
    "python-dateutil",
    "python-dotenv",
    "requests",
    "urllib3",
    "werkzeug",
    "GitPython"
]
EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "flake8",
        "pydocstyle",
        "pytest",
        "pytest-black",
        "pytest-clarity",
        "pytest-dotenv",
        "pytest-flake8",
        "pytest-flask",
        "pre-commit",
    ]
}

setup(
    name="vote",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    maintainer=AUTHOR,
    license="GPL",
    url="https://...",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
