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


@session
def mypy(session) -> None:
    """Runs type checking the package."""
    args = session.posargs or locations
    session.install("mypy",
                    "types-requests",
                    "numpy",
                    "pytest",                    
                    "nox_poetry",
                    "types-toml")    
    session.run("mypy", *args)


@session(python=['3.9', '3.10', '3.11'])
def tests(session) -> None:
    """Run all tests."""
    session.install("pytest",
                    "requests",
                    "pandas")
    session.run("pytest")


@session(python='3.8')
def code_coverage(session) -> None:
    """Run package coverage."""
    pass


@session
def docs(session) -> None:
    """Build the documentation."""
    session.install("sphinx",
                    "sphinx-autodoc-typehints",
                    "cloud-sptheme",
                    "toml")
    session.run("sphinx-build", "-M", "html", "docs", "docs/_build")
