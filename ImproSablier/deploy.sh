# ! bin/bash

# We will wipe all the screen and redeploy them
# Clean

killall screen | echo "No screen to clean"
# Backend
screen -S "BACK" -d -m python3 main.py

# Admin
screen -S "ADMIN" -d -m python3 webapp.py --admin

# Monitoring
screen -S "MONITOR" -d -m python3 webapp.py --monitor

# Public 
screen -S "PUBLIC" -d -m python3 webapp.py