#!/usr/bin/python3
"""
This script generates a .tgz archive
from the contents
of the web_static
"""
from fabric.api import *
from datetime import datetime
from os.path import *
import os

env.hosts = ['3.89.100.88', '54.87.136.71']


def do_pack():
    """
    Method to define the
    propertys
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = 'versions/web_static__{}.tgz'.format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -cvz --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """
    Uncompress the archive to the folder
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split('/')[-1].split('.')[0]
        sudo("mkdir -p  /data/web_static/releases/{}/".format(file))
        sudo("tar xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
             .format(file, file))
        sudo("rm /tmp/{}.tgz".format(file))
        sudo("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(file, file))
        sudo("rm -rf /data/web_static/releases/{}/web_static"
             .format(file))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
             .format(file))
        return True
    except:
        return False


def deploy():
    """
    Full deployment of after task
    """
    archive_path = do_pack()
    if archive_path:
        do_deploy(archive_path)
    else:
        return False
