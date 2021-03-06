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
    if (sys.argv[1] != ""):
        file_path = sys.argv[1]
    else:
        file_path = os.path.join('/tmp', file_name)
        atexit.register(lambda x: os.remove(x) if os.path.exists(x) else None, file_path)
        save = call(['./pngpaste', file_path])
        if save == 1:
            sys.exit()
    return file_path, file_name

def main(wf):
    import boto3
    file_path, file_name = capture()
    bucket_name = os.getenv('bucket_name')
    region_name = os.getenv('region_name')
    namespace = os.getenv('namespace')
    s3 = boto3.client(
        service_name='s3',
        aws_access_key_id=os.getenv('access_key'),
        aws_secret_access_key=os.getenv('secret_key'),
        region_name=region_name,
        endpoint_url="https://%s.compat.objectstorage.%s.oraclecloud.com" %(namespace, region_name)
    )
    s3.upload_file(file_path, bucket_name, file_name, ExtraArgs={'ContentType': "image/png"})
    output = "https://objectstorage.%s.oraclecloud.com/n/%s/b/%s/o/%s" %(region_name,namespace,bucket_name,file_name)
    print (output,end='')

if __name__ == '__main__':
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))
