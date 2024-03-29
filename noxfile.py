from pathlib import Path

import nox

locations = "2017", "2018", "2019", "2020", "2021", "2022", "2023", "noxfile.py"


@nox.session(python="3.10")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", "--target-version=py310", *args)


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


@nox.session(python="3.10")
def mypy(session):
    session.install("mypy")
    if session.posargs:
        session.run("mypy", *session.posargs)
    else:
        for location in locations:
            # mypy 0.910 doesn't yet support match statements
            # see: https://github.com/python/mypy/pull/10191
            if location not in ("2021", "2020", "noxfile.py"):
                session.run("mypy", location)
            else:
                exclude = {"2020": "day12.py", "2021": "day02.py"}
                for year, filename in exclude.items():
                    for day in Path(year).iterdir():
                        if day.name not in (filename, "data", "__pycache__"):
                            session.run("mypy", str(day))


@nox.session(python="3.10")
def tests(session):
    args = session.posargs
    session.install("pytest-timeout")
    session.run("pytest", "-v", *args)
