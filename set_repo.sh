#! /bin/bash

# Create the main package directory for CLI
mkdir mycli

# Create an __init__.py file to make it a Python package
touch mycli/__init__.py

# Create the main CLI file
touch mycli/cli.py

# Create a directory for tests
mkdir tests

# Create a test file for the CLI
touch tests/test_cli.py

# Create a requirements file for dependencies
touch requirements.txt

# Create a .gitignore file and populate it
echo "__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/" > .gitignore
