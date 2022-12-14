from nox_poetry import session

locations = "f1pystats", "tests", "noxfile.py", "docs/conf.py"


@session(python=['3.8'])
def lint(session) -> None:
    """Runs linting for the package."""
    args = session.posargs or locations
    session.install("flake8",
                    "flake8-black",
                    "flake8-import-order",
                    "flake8-bugbear",
                    "flake8-annotations",
                    "flake8-docstrings",
                    "darglint")
    session.run("flake8", *args)


@session(python=["3.8"])
def mypy(session) -> None:
    """Runs type checking the package."""
    args = session.posargs or locations
    session.run("mypy", *args)


@session(python='3.8')
def tests(session) -> None:
    """Run all tests."""
    pass


@session(python='3.8')
def code_coverage(session) -> None:
    """Run package coverage."""
    pass


@session(python="3.8")
def docs(session) -> None:
    """Build the documentation."""
    session.install("sphinx", "sphinx-autodoc-typehints")
    session.run("sphinx-build", "docs", "docs/_build")
