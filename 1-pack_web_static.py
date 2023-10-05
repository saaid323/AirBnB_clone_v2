#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents
of the web_static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    current_time = datetime.now()
    name = "web_static_{}.tgz".format(current_time.strftime("%Y%m%d%H%M%S"))
    local("tar -czvf versions/{} web_static".format(name))
