#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive 
    from the contents of the web_static folder 
"""
from fabric.api import local
from datetime import datetime
import os

filename = "web_static_" + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + ".tgz"

def do_pack():
    """
    Fabric script
    """
    print("Packing web_static to version/{}".format(filename))
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    local("tar -cvzf versions/{} web_static".format(filename))
    print("web_static packed: versions/{} -> {}Bytes".format(filename), os.path.getsize("versions/{}".format(filename)))
