#!/usr/bin/env python

import time, datetime, calendar, yaml, os, shutil
from datetime import date

def main ():
    backup = os.getenv('BACKUP_CONF')
    if not backup:
    	backup = "/home/patg/etc/backup/backup.yaml"

    stream = open(backup)
    conf = yaml.load(stream)
    stream.close()
    
    bucket = conf['s3']['bucket']
    site_name = conf['site_name']
    backup_name = conf['backup_name']
    backup_dir = conf['backup_dir']
    secret = conf['secret']
    
def tstamp ():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
   main()
