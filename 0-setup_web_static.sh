#!/usr/bin/env bash
# Setup the web servers to the deployment of web_static

#installl nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# create directory tree
if [[ ! -e "$/data/web_static/releases/test/index.html" ]]; then
    sudo mkdir -p /data/
    mkdir /data/web_static/
    mkdir /data/web_static/releases/
    sudo mkdir /data/web_static/shared/
    mkdir /data/web_static/releases/test/
    echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
fi
#created a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#ownership
sudo chown -R ubuntu:ubuntu /data/
#Update the Nginx configuration
sudo sed -i '48i \\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
#Restar service ngninx
sudo service nginx start
