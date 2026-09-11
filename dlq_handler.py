import json
import logging

def handle_dead_letter(event, context):
    for record in event['Records']:
        logging.error(f"Failed message: {record['body']}")
    return {'status': 'processed_dlq'}
