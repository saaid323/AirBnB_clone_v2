#!/usr/bin/python3
"""abric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy """
from fabric.api import run, put, env, local
from datetime import datetime
import os
env.hosts = ['100.25.23.226', '54.90.28.30']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    current_time = datetime.now()
    name = "web_static_{}.tgz".format(current_time.strftime("%Y%m%d%H%M%S"))
    local("tar -czvf versions/{} web_static".format(name))


def do_deploy(archive_path):
    """script (based on the file 1-pack_web_static.py) that distributes an
    archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    archive_filename = os.path.basename(archive_path)
    print(archive_filename)
    folder_name = "/data/web_static/releases/{}".format(
        archive_filename.split('.')[0]
        )
    run("mkdir -p {}".format(folder_name))
    run("tar -xzf /tmp/{} -C {}".format(archive_filename, folder_name))
    run("mv {0}/web_static/* {0}/".format(folder_name))
    run("rm -rf {}/web_static".format(folder_name))
    run("rm /tmp/{}".format(archive_filename))
    current_link = "/data/web_static/current"
    run("rm -f {}".format(current_link))
    run("ln -s {} {}".format(folder_name, current_link))
    return True


def deploy():
    """script (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers, using the
    function deploy"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)


def do_clean(number=0):
    """deletes out-of-date archives"""
    path = "versions"
    file_list = os.listdir(path)
    if number == 0 or number == 1:
        for i in file_list[:-1]:
            file_path = os.path.join(path, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                run("rm -rf {}".format(file_path))
    else:
        for i in file_list[:number]:
            file_path = os.path.join(path, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
                run("rm -rf {}".format(file_path))
