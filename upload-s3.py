#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
import os
import sys
import atexit
import imghdr
from subprocess import call
from os.path import expanduser, exists, basename, getsize
from workflow import Workflow

def capture():
    file_name = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S.png')
    file_path = os.path.join('/tmp', file_name)
    atexit.register(lambda x: os.remove(x) if os.path.exists(x) else None, file_path)
    save = call(['./pngpaste', file_path])
    if save == 1:
        sys.exit()
    return file_path, file_name

def main(wf):
    import boto3
    if sys.argv.__len__() == 1:
        file_path, file_name = capture()
    else:
        file_path = expanduser(sys.argv[-1])
        if not exists(file_path):
            file_path, file_name = capture()
        else:
            if imghdr.what(file_path) not in ['jpeg', 'jpg', 'png']:
                sys.exit('file type error')
            file_name = basename(file_path)
    bucket_name = os.getenv('bucket_name')
    region_name = os.getenv('region_name')
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('access_key'),
        aws_secret_access_key=os.getenv('secret_key')
    )
    s3.upload_file(file_path, bucket_name, file_name, ExtraArgs={'ContentType': "image/png"})
    output = "https://s3-%s.amazonaws.com/%s/%s" %(region_name, bucket_name, file_name)
    print (output,end='')

if __name__ == '__main__':
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))