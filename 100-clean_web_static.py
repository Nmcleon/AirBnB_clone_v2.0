#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""
import os
from fabric.api import *

env.hosts = ['54.157.179.122', '100.26.234.54']  # server IP addresses


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = 1 if int(number) == 0 else int(number)

    local_archives = sorted(os.listdir("versions"))
    [local_archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in local_archives]

    with cd("/data/web_static/releases"):
        local_archives = run("ls -tr").split()
        local_archives = [a for a in local_archives if "web_static_" in a]
        [local_archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in local_archives]
