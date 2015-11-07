###################################################################
#
# Deployment script for digital ocean servers
#
# Usage: fab <server> refresh
# <server> = dev, stage, prod
#
####################################################################

from fabric.api import local, run, env, put, cd, prefix, sudo
import os, time

# remote ssh credentials
env.hosts = []
env.user = ''
env.password = '' #ssh password for user
# or, specify path to server public key here:
# env.key_filename = 'C:\Users\Name\.ssh\id_rsa'


def local_rob():
    settings = 'academy.settings.local_settings'
    print('Local Rob')
    local('./manage.py migrate --settings={0}'.format(settings))




