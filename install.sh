#!/usr/bin/env bash




# setup git and virtualenvs
apt-get update
apt-get install python-pip -y
apt-get install python-dev libjpeg-dev -y
apt-get install git -y
pip install virtualenv virtualenvwrapper

virtualenv env