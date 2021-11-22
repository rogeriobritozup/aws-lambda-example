import requests
import json

def proccess_sqs_record(record):
    sqs_body = json.loads(record["body"])
    url = sqs_body["url"]
    print("requesting url {}".format(url))
    r = requests.get(url)
    print("response code: {}".format(r.status_code))
    print("response body: {}".format(r.json()))

def handler(event, context):
    records = event["Records"]
    
    for record in records:
        try:
            proccess_sqs_record(record)
        except Exception as e:
            print("error on procces sqs record: {}".format(e))