#!/bin/bash

# Change directory to the script's location
cd "$(dirname "$0")" || exit

# Check if venv exists, if not create it
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Set PYTHONPATH to include the top-level project folder
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Run main.py
python3 src/main.py
