#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Just testing the servers of Tarik Horaichi.
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

string_for_replacement="listen 80 default_server;\n\tlocation /hbnb_static { alias /data/web_static/current/;}"
sudo sed -i "s.listen 80 default_server;.$string_for_replacement." /etc/nginx/sites-enabled/default

sudo service nginx restart
