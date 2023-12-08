#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
"""

from fabric.api import local, run, env
from datetime import datetime
from os.path import exists

env.hosts = ['54.157.179.122', '100.26.234.54']  # server IP addresses
env.user = 'ubuntu'  # username
env.key_filename = '/~/.ssh/school'  # SSH private key path


def do_pack():
    """
    Archives static files
    """
    time = datetime.now()
    archive = 'versions/web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf {} web_static'.format(archive))
    if create.succeeded:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    folder_name = '/data/web_static/releases/' + file_name.split('.')[0]

    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(folder_name))
    run('tar -xzf /tmp/{} -C {}'.format(file_name, folder_name))
    run('rm /tmp/{}'.format(file_name))
    run('mv {}/web_static/* {}'.format(folder_name, folder_name))
    run('rm -rf {}/web_static'.format(folder_name))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(folder_name))

    return True


def deploy():
    """
    Deploys an archive to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
