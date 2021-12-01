import nox

locations = "2019", "2020", "2021", "noxfile.py"


@nox.session(python="3.10")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python="3.10")
def isort(session):
    args = session.posargs or locations
    session.install("isort")
    session.run("isort", *args)


@nox.session(python="3.10")
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-isort", "flake8-bugbear")
    session.run("flake8", *args)
