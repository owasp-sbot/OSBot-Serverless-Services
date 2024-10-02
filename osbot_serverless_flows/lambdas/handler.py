
def run(event, context):
    print("******* in the lambda function ***** ")
    return {
        'statusCode': 200,
        'body': 'Hello from main code Lambda!'
    }
