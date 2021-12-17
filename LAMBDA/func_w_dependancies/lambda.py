import requests as req
import json


def lambda_handler(event, context):

    resp = req.get("http://www.webcode.me")

    print(resp.text)
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
