import requests
import json

'''
{
    "Records": [
        {
            "messageId": "efaad907-22ed-4a58-a9de-5ac94f9aa0bc",
            "receiptHandle": "AQEBUTYJXE1h7sN0tEZIG7TNLE1RfCXame5bsXWIucAryERxPyrr8f5kHXEJXjwP+z488QoSd8rreUHvMd7+Cr8cfQ6jvCUGUVvQP7zuLQ6e8zI8S4OvTtdLMBcrkTFss3AwwhrMm3f2R4oVAI8XnWWOBdOONukASjut+gccDK08r/QzR3dk8flJF9sSAxOlmRj0UuoFycmVpRBxBTw2ORScTKHB4zPRUqYukF2p08fChYu0VGLcgW1UW2X+r2NgPRdZ0wWPR3QD+Ucppp1cl0lLj8SR+Qa7o9jrhSNedfTBO+ATm0IMEwEmSvyo2eiZ6CMXWEDYplx9R65Cuf8xZAko7Ni17PLwrDrROSUo8k/9l1HJUGbYzh6fyc5FyhF2dEnev2mfu4naceSdcUHTtmssFw==",
            "body": "{\n\"url\": \"https://jsonplaceholder.typicode.com/posts\"\n}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1637670522981",
                "SenderId": "113575749776",
                "ApproximateFirstReceiveTimestamp": "1637670522983"
            },
            "messageAttributes": {},
            "md5OfBody": "75d801ce7f994bda87ef5963c26f4998",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:113575749776:make-requests-topic",
            "awsRegion": "us-east-2"
        }
    ]
}
'''

def proccess_sqs_record(record):
    sqs_body_str = record["body"]
    sqs_body_dict = json.loads(sqs_body_str)
    url = sqs_body_dict["url"]
    print("requesting url {}".format(url))
    r = requests.get(url)
    print("response code: {}".format(r.status_code))
    print("response body: {}".format(r.json()))

def lambda_handler(event, context):
    records = event["Records"]
    
    for record in records:
        try:
            proccess_sqs_record(record)
        except Exception as e:
            print("error on procces sqs record: {}".format(e))
            return {
                "success": False
            }

    return {
        "success": True
    }