#!/bin/bash

# Get the current directory
PROJECT_DIR="$(pwd)"

# Name of the virtual environment
VENV_NAME="venv"

# Create the virtual environment
python3 -m venv "$PROJECT_DIR/$VENV_NAME"

echo "activate: source $PROJECT_DIR/$VENV_NAME/bin/activate"