#!/bin/bash

cd PuckPuzzle
. .PPvenv/bin/activate
python manage.py create_daily_game
git add .
git commit -m "Daily game"
git push origin main