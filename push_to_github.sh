#!/bin/bash
while ! ping -c 1 -W 1 8.8.8.8; do
    sleep 1
done

cd PuckPuzzle
. .PPvenv/bin/activate
python manage.py create_daily_game
git add .
git commit -m "Daily game"
git push origin main
osascript -e 'display notification "PuckPuzzle was reset!" with title "PuckPuzzle"'