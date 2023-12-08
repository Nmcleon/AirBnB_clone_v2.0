#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import local, run, env

env.hosts = ['54.157.179.122', '100.26.234.54']  # server IP addresses
env.user = 'ubuntu'  # username
env.key_filename = '/~/.ssh/school'  # SSH private key path


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 1:
        number = 1
    number += 1

    local_archives = local('ls -t versions', capture=True).split('\n')
    for i in range(number, len(local_archives)):
        local('rm -f versions/{}'.format(local_archives[i]))

    run_archives = run('ls -t /data/web_static/releases').split('\n')
    for i in range(number, len(run_archives)):
        run('rm -f /data/web_static/releases/{}'.format(run_archives[i]))
