#!/usr/bin/python3
from fabric.api import env, run

host = ['54.198.56.98', '35.153.232.194']
env.hosts = host
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

def test():
    run('ls -la')

test()
