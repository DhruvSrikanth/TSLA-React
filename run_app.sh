#!/bin/bash

echo "Installing Requirements..."
pip3 install -r requirements.txt
echo "Requirements Installed!"

echo "Activating Virtual Environment..."
source venv/bin/activate
echo "Virtual Environment Activated!"

echo "Running app.py:"
python3 ./src/app.py