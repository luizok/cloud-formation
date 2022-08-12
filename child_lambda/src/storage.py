import os

import boto3


BUCKET_NAME = os.getenv('BUCKET_NAME')


def write_file(filename):

    if not filename.endswith('.txt'):
        return False

    with open(f'/tmp/{filename}', 'w') as file:
        file.write(filename[:-4])

    s3_client = boto3.resource('s3')
    bucket = s3_client.Bucket(BUCKET_NAME)

    bucket.upload_file(f'/tmp/{filename}', filename)

    return True
