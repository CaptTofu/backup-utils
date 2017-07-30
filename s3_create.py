#!/usr/bin/env python

import time, datetime, calendar, s3fs, yaml, os, shutil
from datetime import date


def main ():
    stream = open("/etc/backup/backup.yaml", "r")
    conf = yaml.load(stream)
    stream.close()
    
    bucket = conf['s3']['bucket']

    site_name = conf['site_name']
    backup_name = conf['backup_name']
    backup_dir = conf['backup_dir']
    secret = conf['secret']
    aws_key = conf['s3']['key']
    aws_secret = conf['s3']['secret']
    
    s3 = s3fs.S3FileSystem(key=aws_key, secret=aws_secret)
    
    if not s3.exists(bucket):
        print "making bucket %s\n" % bucket
        s3.mkdir(bucket)

if __name__ == "__main__":
   main()
