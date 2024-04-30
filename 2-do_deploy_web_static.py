#!/usr/bin/python3
""" Deploy web static package """
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['3.86.13.247', '35.174.208.1']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """ Deploy to webservers """
    try:
        if not (path.exists(archive_path)):
            return False

        file_name = archive_path.split("/")[-1]

        no_ext = archive_path.split("/")[-1].strip('.tgz')

        run('sudo mkdir -p tmp')

        # Upload the archive to the /tmp
        put(archive_path, '/tmp/')
        new_path = "/tmp/{}".format(file_name)

        # Create dest dir
        unc_path = 'data/web_static/releases/{}/'.format(no_ext)
        run('sudo mkdir -p {}'.format(unc_path))
        # Uncompress the archive
        run("sudo tar -xzf {} -C {}".format(new_path, unc_path))
        # Delete the archive
        run("sudo rm {}".format(new_path))
        # Move contents into host web_static
        run('sudo mv ./{}web_static/* ./{}'.format(unc_path, unc_path))
        # Delete extra dir
        run('sudo rm -rf ./{}web_static/'.format(unc_path))
        # Delete symlink
        run('sudo rm -rf /data/web_static/current')
        # Create symlink
        run('sudo ln -s /{} /data/web_static/current'.format(unc_path))

    except Exception:
        return False

    # return True on success
    return True
