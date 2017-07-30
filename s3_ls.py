#!/usr/bin/env python

import s3fs
import yaml
import os


stream = open("/etc/backup/backup.yaml", "r")
conf = yaml.load(stream)
stream.close()
bucket = conf['s3']['bucket']

s3fs = s3fs.S3FileSystem(anon=False)

files = s3fs.ls(bucket)

for file in files:
    filesize = s3fs.du(file)
    print "%s %d\n" % (file, filesize[file])
