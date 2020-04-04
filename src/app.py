import hashlib
import json
import boto3
from os import getenv

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    with open('/tmp/ids.csv', 'wb') as data:
        s3.download_fileobj('lambda-coldstart', 'ids.csv', data)

    with open('/tmp/ids.csv', 'r') as data:
        content = data.readlines()

    content = [c[:-1] for c in content]

    sha = hashlib.sha256()
    for c in content:
        sha.update(c.encode())

    print('completed')

    return {
            "statusCode": 200,
            "body": json.dumps({
                "result": "completed",
            }),
        }


def warmup(event, context):
    client = boto3.client('lambda')
    client.invoke(FunctionName=getenv('TargetFunction'),
                  InvocationType='Event',
                  Payload="{}".encode('ascii'))
