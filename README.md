# Alfred Workflow: Upload Screenshot to Oracle Cloud Object storage using s3 compatible API.

This workflow helps you upload screenshot in your clipboard or local disk to S3 and put the public url of the image to your clipboard.

## Overview

This workflow is written in Python. And used Boto3 as AWS client to upload image.

## Download

https://github.com/PatelUtkarsh/Alfred-Workflow-Upload-S3/releases

## Usage

Check https://www.ateam-oracle.com/aws-s3-to-oci-access-best-practices on how to get environment variables.

Config Environment Variables:

- access_key: Oracle access key
- secret_key: Oracle access secret
- region_name: Oracle cloud region name
- bucket_name: Oracle bucket name. e.g. `my-bucket-name`
- namespace: Oracle namespace.

Upload image from clipboard:

```bash
upload
```

Upload image from local:

```bash
upload TYPE-FILENAME-HERE
```

## Forked source: 🙌
- https://github.com/tonyxu-io/Alfred-Workflow-Upload-S3 