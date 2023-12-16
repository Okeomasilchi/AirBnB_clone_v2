#!/usr/bin/python3
"""this model holds the do_pack function
"""


from fabric.api import local
from datetime import datetime
import os


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
