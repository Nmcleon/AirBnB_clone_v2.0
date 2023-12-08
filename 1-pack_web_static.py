#!/usr/bin/python3
"""Fabric script that generates a .tgz
archive from the contents of the web_static"""

import os
from datetime import datetime
from fabric.api import local

def do_pack():
  """
  Creates a .tgz archive from the contents of web_static folder
  """
  time = datetime.now()
  archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
  local('mkdir -p versions')
  create = local('tar -cvzf versions/{} web_static'.format(archive))
  if create is None:
    return archive
  else:
    return None
