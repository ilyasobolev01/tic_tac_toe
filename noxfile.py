"""
Nox sessions for automated quality checks and testing.

This file defines a set of sessions that can be run by the Nox automation tool.
These sessions are used for:
- Running the test suite against multiple Python versions.
- Checking code style and formatting with linters (Flake8, Black).
- Performing static type analysis with Mypy.

These tasks are used both for local development and in the CI/CD pipeline
to ensure code quality and correctness.
"""

# Source: https://nox.thea.codes/en/stable/

import nox

# Sets the default sessions to run when `nox` is called without arguments.
nox.options.sessions = ["tests", "lint"]

PYTHON_VERSIONS = ["3.8", "3.10", "3.11"]


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite with pytest."""
    session.install("poetry")
    session.run("poetry", "install", "--no-interaction")
    session.run("poetry", "run", "pytest")


@nox.session(python=PYTHON_VERSIONS[-1])
def lint(session):
    """Lint with flake8 and check formatting with black."""
    # The src and tests directories are specified for linting.
    args = session.posargs or ["src", "tests"]
    session.install("black", "flake8")
    session.run("flake8", *args)
    session.run("black", "--check", *args)


@nox.session(python=PYTHON_VERSIONS[-1])
def typing(session):
    """Type-check using mypy."""
    # Mypy needs project dependencies to be installed.
    session.install("poetry")
    session.run("poetry", "install", "--no-interaction")
    session.install("mypy")
    session.run("mypy", "src")