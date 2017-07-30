#!/usr/bin/env python

import s3fs
import yaml
import re
import os
from datetime import date
import calendar

stream = open("/etc/backup/backup.yaml", "r")
conf = yaml.load(stream)
stream.close()

bucket = conf['s3']['bucket']
site_name = conf['site_name']
backup_name = conf['backup_name']
backup_dir = conf['backup_dir']
restore_dir = conf['restore_dir']
secret = conf['secret']
aws_key = conf['s3']['key']
aws_secret = conf['s3']['secret']

bak_date = date.today()
day_name = calendar.day_abbr[bak_date.weekday()]

archive_file = backup_name +  ".tar.gz"
enc_file = archive_file + "." + day_name + '.enc'

os.chdir(restore_dir)

s3fs = s3fs.S3FileSystem(key=aws_key, secret=aws_secret)

files = s3fs.ls(bucket)

print "this is a list of files on s3:\n"
i = 0;
for file in files:
    print "%d: %s\n" % (i, file) 
    i = i + 1

file_num = int(raw_input("select the number of the file you want to download and decrypt: "))

enc_file = files[file_num]
decr_file = re.sub('\.enc$', '', enc_file)
bregex = "^%s/" % bucket
local_enc_file = restore_dir + "/" + re.sub(bregex, "", enc_file)
decr_file = restore_dir + "/" + re.sub(bregex, "", decr_file)
print "decr_file %s" % decr_file


print "The file to download is %s, starting download.\n" % enc_file
s3fs.get(enc_file, local_enc_file)

decr_command = 'openssl enc -aes-256-cbc -d -in %s -out %s -kfile "%s"' % (local_enc_file, decr_file, secret)
print "decrypting the backup: %s\n" % decr_command
os.system(decr_command)

print "done.\n"
