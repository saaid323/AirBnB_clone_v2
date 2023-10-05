#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
if ! dpkg -l | grep -q "nginx"; then
        sudo apt-get -y update
        sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<html><head></head><body>Hello, web_static!</body></html>" >  /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80;
    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}" >  /etc/nginx/sites-available/default

sudo service nginx restart
