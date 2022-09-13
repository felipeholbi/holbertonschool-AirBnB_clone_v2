#!/usr/bin/env bash

# Install Nginx if it not already installed
sudo apt-get -y update;
sudo apt-get -y upgrade;
sudo apt-get -y install nginx;

# Create folders if it doesn't already exist
sudo mkdir /data/
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

# Create a fake HTML file
    echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
    </html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '48i \\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restar service Ngnix
sudo service nginx restart;
