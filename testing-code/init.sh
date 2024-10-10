#!/bin/bash

# Get the current directory
PROJECT_DIR="$(pwd)"

# Name of the virtual environment
VENV_NAME="venv"

# Create the virtual environment
if python3 -m venv "$PROJECT_DIR/$VENV_NAME"; then
    echo "Virtual environment created successfully."
    echo "To activate it, run: source $PROJECT_DIR/$VENV_NAME/bin/activate"
else
    echo "Failed to create virtual environment." >&2
    exit 1
fi

