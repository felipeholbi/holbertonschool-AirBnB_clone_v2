#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static"""
from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """Generate tgz file"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz = "versions/web_static_{}.tgz".format(date)
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        local("tar -cvzf {} web_static".format(tgz))
        return tgz
    except Exception:
        return None
