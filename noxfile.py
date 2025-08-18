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


nox.options.sessions = ["tests", "lint"]

PYTHON_VERSIONS = ["3.8", "3.10", "3.11"]


def export_requirements(session):
    session.run(
        "poetry",
        "export",
        "--with",
        "dev",
        "--format",
        "requirements.txt",
        "--output",
        "requirements.txt",
        "--without-hashes",
        external=True,
    )


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite with pytest."""
    export_requirements(session)
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    session.run("pytest")


@nox.session(python=PYTHON_VERSIONS[-1])
def lint(session):
    """Lint with flake8 and check formatting with black."""
    args = session.posargs or ["src", "tests"]
    session.install("black", "flake8")
    session.run("flake8", *args)
    session.run("black", "--check", *args)


@nox.session(python=PYTHON_VERSIONS[-1])
def typing(session):
    """Type-check using mypy."""
    export_requirements(session)
    session.install("-r", "requirements.txt")
    session.install("-e", ".")
    session.install("mypy")
    session.run("mypy", "src", "tests")
