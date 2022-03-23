#!/bin/bash

echo "Activating Virtual Environment..."
source ./venv/bin/activate
echo "Virtual Environment Activated!"

echo "Running app.py:"
python3 ./src/app.py