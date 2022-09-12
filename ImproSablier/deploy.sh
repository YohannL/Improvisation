#!/bin/bash

# Change target IP:
git checkout -- WebApp/admin/static/public.js WebApp/public/static/public.js WebApp/monitor/static/public.js
sed -i 's/192.168.1.34/51.91.101.229/g' WebApp/admin/static/public.js
sed -i 's/192.168.1.34/51.91.101.229/g' WebApp/public/static/public.js
sed -i 's/192.168.1.34/51.91.101.229/g' WebApp/monitor/static/public.js


# We will wipe all the screen and redeploy them
# Clean

killall screen || echo "No screen to clean"
# Backend
echo "BACK END DEPLOY--------------"
screen -S "BACK" -d -m python3 main.py

# Admin
echo "ADMIN DEPLOY-----------------"
screen -S "ADMIN" -d -m python3 webapp.py --admin

# Monitoring
echo "MONITOR DEPLOY---------------"
screen -S "MONITOR" -d -m python3 webapp.py --monitor

# Public
echo "PUBLIC DEPLOY----------------"
screen -S "PUBLIC" -d -m python3 webapp.py

# Display all the present screen"
screen -ls


#if you want to access to one screen do :
echo "screen -R BACK     # to access to the back sub sh"
echo "screen -R ADMIN    # to access to the admin sub sh"
echo "screen -R MONITOR  # to access to the monitor sub sh"
echo "screen -R PUBLIC   # to access to the public sub sh"
