import os
import datetime as dt

import boto3


BUCKET_NAME = os.getenv('BUCKET_NAME')


def write_file(filename):

    with open(f'/tmp/{filename}', 'w') as file:
        file.write(filename[:-4])

    s3_client = boto3.resource('s3')
    bucket = s3_client.Bucket(BUCKET_NAME)

    bucket.upload_file(f'/tmp/{filename}', filename)


def handler(event, context):

    timestamp = dt.datetime.now().timestamp()
    filename = f'file_{timestamp}.txt'

    write_file(filename)
    print('Child:', event)

    return {
        'httpStatus': 200,
        'body': {'some': 'data'}
    }
