import os
import json
import boto3


def handler(event, context):
    print('Parent:', event)

    lambda_client = boto3.client('lambda')
    lambda_client.invoke(
        FunctionName=os.environ.get('CHILD_LAMBDA_ARN'),
        InvocationType='Event',
        Payload=json.dumps({'parentData': 'Im gonna call my child'})
    )

    return {
        'httpStatus': 200,
        'body': {'some': 'data'}
    }
