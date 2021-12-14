# https://github.com/amazon-archives/serverless-app-examples
# https://github.com/amazon-archives/serverless-app-examples/blob/master/python/hello-world-python3/lambda_function.py
import json

print("Loading function")


def lambda_handler(event, context):
    return "Hello World"
