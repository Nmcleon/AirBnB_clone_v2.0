#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""

from fabric.api import *
from os.path import exists

env.hosts = ['54.157.179.122', '100.26.234.54']  # server IP addresses
env.user = 'ubuntu'  # server username
env.key_filename = '/root/.ssh/school'  # SSH private key path


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    folder_name = '/data/web_static/releases/' + file_name.split('.')[0]

    put(archive_path, '/tmp/')
    run('sudo mkdir -p {}'.format(folder_name))
    run('sudo tar -xzf /tmp/{} -C {}'.format(file_name, folder_name))
    run('sudo rm /tmp/{}'.format(file_name))
    run('sudo mv {}/web_static/* {}'.format(folder_name, folder_name))
    run('sudo rm -rf {}/web_static'.format(folder_name))
    run('sudo rm -rf /data/web_static/current')
    run('sudo ln -s {} /data/web_static/current'.format(folder_name))

    return True
