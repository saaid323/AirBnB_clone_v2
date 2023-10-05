#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html><head></head><body>Hello, web_static!</body></html>" >  /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
echo "server {
    listen 80;
    server_name _;
    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}" >  /etc/nginx/sites-available/default

sudo service nginx restart
