import os

bind = "0.0.0.0:8208"
workers = 4
# env = None
# max-requests = None
# user = user
# group = group
logfile = "/var/log/thumbtack/thumbtack.log"
# loglevel = debug
IMAGE_DIR = os.getcwd()
# IMAGE_DIR = '/vagrant/tests/test_images'
MOUNT_DIR = '/mnt/thumbtack'
DATABASE = 'database.db'
