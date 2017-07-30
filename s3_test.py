#!/usr/bin/env python

import s3fs
import yaml
import os


stream = open("/etc/backup/backup.yaml", "r")
conf = yaml.load(stream)
stream.close()
bucket = conf['s3']['bucket']

s3fs = s3fs.S3FileSystem(anon=False)

# Get file info
source_path= '/opt/data/backups/mysite-mysql.tar.gz.enc'
source_size = os.stat(source_path).st_size
print "source size: %d\n" % source_size
#
s3fs.put(source_path, bucket + '/mysite-mysql.tar.gz.enc')

print "dest size: %d\n" % s3fs.du(bucket + '/mysite-mysql.tar.gz.enc')
