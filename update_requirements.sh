#!/bin/bash

echo "Updating requirements..."
pip3 freeze > requirements.txt
echo "requirements.txt Updated!"

echo "Updating git..."
git add .
git commit -m "updated requirements"
git push origin master:master
echo "git updated!"