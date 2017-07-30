#!/usr/bin/env python

import s3fs
import yaml

stream = open("/etc/backup/backup.yaml", "r")
conf = yaml.load(stream)
stream.close()

bucket = conf['s3']['bucket']
aws_key = conf['s3']['key']
aws_secret = conf['s3']['secret']

print "listing bucket %s" % bucket
s3 = s3fs.S3FileSystem(key=aws_key, secret=aws_secret)

objects = s3.ls(bucket, detail=True)

for object in objects:
    print "%s size %s date %s" % (object['Key'], object['Size'], str(object['LastModified']))
