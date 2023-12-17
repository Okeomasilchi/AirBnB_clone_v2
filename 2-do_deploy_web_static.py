#!/usr/bin/python3
"""this model holds the do_pack function
"""


from fabric.api import local, env, put, run
from datetime import datetime
import os

host = ['54.198.56.98', '35.153.232.194']
env.hosts = host
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        (str): Archive path if generated successfully, None otherwise.
    """
    local("mkdir -p versions")

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(timestamp)

    result = local("tar -cvzf versions/{} \
                   web_static".format(archive_name), capture=True)

    if result.succeeded:
        archive_path = os.path.join("versions", archive_name)
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        file_name = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}". \
            format(file_name.split(".")[0])
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_name))

        run("rm /tmp/{}".format(file_name))

        run("rm -f /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(folder_name))
        return True

    except Exception as e:
        return False
