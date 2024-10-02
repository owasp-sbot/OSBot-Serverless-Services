from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows


def run(event, context):
    print("******* in the lambda function ***** ")
    message = f'Hello from main code Lambda! | version: {version__osbot_serverless_flows}'
    return {
        'statusCode': 200,
        'body': message
    }
