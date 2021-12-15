# https://github.com/amazon-archives/serverless-app-examples
# https://github.com/amazon-archives/serverless-app-examples/blob/master/python/hello-world-python3/lambda_function.py
import json


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
    respond(None, res="hello world!")