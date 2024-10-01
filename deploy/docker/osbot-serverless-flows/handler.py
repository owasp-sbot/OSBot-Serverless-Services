# handler.py

import sys
# def lambda_handler(event, context):
#     return 'Hello from AWS Lambda using Python' + sys.version + '!'

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Docker Lambda!'
    }
