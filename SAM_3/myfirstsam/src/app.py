# https://github.com/amazon-archives/serverless-app-examples
# https://github.com/amazon-archives/serverless-app-examples/blob/master/python/hello-world-python3/lambda_function.py
import json
import os
import boto3

# create client outside of the handler
region_name = os.environ["REGION_NAME"]
dynamo = boto3.client("dynamodb", region_name=region_name)
table_name = os.environ["TABLE_NAME"]


def respond(err, res=None):
    return {
        "statusCode": "400" if err else "200",
        "body": err.message if err else json.dumps(res),
        "headers": {
            "Content-Type": "application/json",
        },
    }


def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    scan_result = dynamo.scan(Tablename=table_name)
    return respond(None, res=scan_result)