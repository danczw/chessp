# **chess-p**

Simple chess game implemented in Python. Two players can play against each other.

<br>

-----------------

<br>

## Setup

[Poetry](https://python-poetry.org) is used to manage the project dependencies. Install dependencies via:

    `poetry install`

Simply start a new game with:

    `python3 src/main.py`

<br>

-----------------

<br>

## Development setup

Various pre-commit hooks are implemented to ensure code quality. After development environment is set up and activated, install them via:

    `pre-commit install`

These hooks are run automatically when committing changes. To run them manually, use:

    `pre-commit run --all-files -v`

Currently, following hooks are included:

- `black`: code formatter
- `flake8`: linter
- `pytest`: unit tests
- `coverage` & `pytest-cov`: code coverage
