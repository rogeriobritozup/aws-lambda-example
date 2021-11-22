import requests
import json

def handler(event, context):
    records = event["Records"]
    for record in records:
        sqs_body = json.loads(record["body"])
        url = sqs_body["url"]
        print("requesting url {}".format(url))
        r = requests.get(url)
        print("response code: {}".format(r.status_code))
        print("response body: {}".format(r.json()))