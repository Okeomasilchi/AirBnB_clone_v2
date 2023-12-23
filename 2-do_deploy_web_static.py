#!/usr/bin/python3
"""this model holds the do_pack function
"""


from fabric.api import local, env, put, run
from datetime import datetime
import os
from fabric.connection import Connection

host = ['54.198.56.98', '35.153.232.194']
env.hosts = host
env.user = "ubuntu"



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

for host in env.hosts:
    c = Connection(host=host, user=env.user, connect_kwargs={"key_filename": "~/.ssh/id_rsa"})
    c.run('uname -s')
