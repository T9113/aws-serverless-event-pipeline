import json
import boto3

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('EventsTable')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['body'])
        table.put_item(Item=payload)
    return {'status': 'success'}
