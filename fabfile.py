import os
import datetime
import time
from fabric.api import *

env.hosts = ['marc@50.116.4.99']

def host_type():
  run('uname -s')

def deploy():
  code_dir = '/home/jrcoyle/SUMSarizer'
  with cd(code_dir):
    run("git pull")
    sudo("supervisorctl restart all")

# TODO: Migrations
  # run alembic on db

def snapshot():
  snapshot_dir = '/home/www'
  outdir = 'dumps'
  outfilename = "dump-%s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S')
  outpath = os.path.join(outdir, outfilename)
  with cd(snapshot_dir):
    sudo('pg_dump -Fc --no-acl --no-owner sums > mydb.dump', user='www')
  get('/home/www/mydb.dump', outpath)