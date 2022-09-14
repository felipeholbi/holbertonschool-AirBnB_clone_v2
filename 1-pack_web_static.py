#!/usr/bin/python3
"""
This script generates a .tgz archive
 from the contents
of the web_static
"""
from fabric.api import local
from datetime import datetime


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
