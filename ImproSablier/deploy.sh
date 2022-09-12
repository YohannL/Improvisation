#!/bin/bash

# We will wipe all the screen and redeploy them
# Clean

killall screen || echo "No screen to clean"
# Backend
echo "\nBACK END DEPLOY--------------"
screen -S "BACK" -d -m python3 main.py

# Admin
echo "\nADMIN DEPLOY-----------------"
screen -S "ADMIN" -d -m python3 webapp.py --admin

# Monitoring
echo "\nMONITOR DEPLOY---------------"
screen -S "MONITOR" -d -m python3 webapp.py --monitor

# Public
echo "\nPUBLIC DEPLOY----------------"
screen -S "PUBLIC" -d -m python3 webapp.py

# Display all the present screen"
screen -ls


#if you want to access to one screen do :
# screen -R BACK     # to access to the back sub sh
# screen -R ADMIN    # to access to the admin sub sh
# screen -R MONITOR  # to access to the monitor sub sh
# screen -R PUBLIC   # to access to the public sub sh
