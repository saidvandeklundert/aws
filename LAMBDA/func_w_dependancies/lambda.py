import requests as req
import os


def lambda_handler(event, context):
    resp = req.get("https://whatismyipaddress.com/")
    ret = ""
    for line in resp.text.splitlines():
        if "your ip address" in line.lower():
            ret = line
    for k, v in sorted(os.environ.items()):
        print(k, v)
    return {"statusCode": 200, "body": ret}