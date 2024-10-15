from unittest import TestCase
from dotenv import load_dotenv
from osbot_utils.utils.Misc import random_text, wait_for

from deploy.test_aws_events.handler import run
from osbot_aws.deploy.Deploy_Lambda import Deploy_Lambda
from osbot_local_stack.testing.TestCase__Local_Stack__Temp_Lambda import LAMBDA__DEPENDENCIES__REQUESTS

from osbot_utils.utils.Dev import pprint
from osbot_aws.aws.s3.S3 import S3
from osbot_utils.utils.Env import get_env
from osbot_aws.AWS_Config import aws_config


class test___events_on_live_aws(TestCase):

    def setUp(self):
        load_dotenv()
        region_name = 'eu-west-2'
        aws_config.set_aws_session_account_id  (get_env('AWS_ACCOUNT_ID__654654216424'       ))
        aws_config.set_aws_session_region_name (region_name                                   )
        aws_config.set_aws_access_key_id       (get_env('AWS_ACCESS_KEY_ID__654654216424'    ))
        aws_config.set_aws_secret_access_key   (get_env('AWS_SECRET_ACCESS_KEY__654654216424'))

    def test_create_lambda(self):
        deploy_lambda = Deploy_Lambda(run)
        # deploy_lambda.add_osbot_utils()
        # deploy_lambda.add_modules(LAMBDA__DEPENDENCIES__REQUESTS)
        # pprint(deploy_lambda.deploy())
        payload = {'from unit test': 'some data'}
        pprint(deploy_lambda.invoke(payload))

    def test_set_event_hooks(self):
        deploy_lambda = Deploy_Lambda(run)
        bucket_name   = deploy_lambda.osbot_setup.s3_bucket_lambdas
        function_arn  = deploy_lambda.lambda_function().function_arn()
        s3 = S3()
        pprint(s3.bucket_notification(bucket_name))
        notification_config = { 'LambdaFunctionConfigurations': [{ 'LambdaFunctionArn': function_arn,
                                                                    'Events'          : ['s3:ObjectCreated:*',
                                                                                         's3:ObjectRemoved:*'] } ] }
        s3 = S3()
        print(bucket_name)
        #pprint(function_arn)
        #pprint(s3.buckets())

        result__allow_function_invoke = s3.bucket_notification_set_lambda_permission(function_arn)
        result__set_event = s3.bucket_notification_create(s3_bucket=bucket_name, notification_config=notification_config)
        pprint(result__allow_function_invoke)
        pprint(result__set_event)

        # result = s3.client().put_bucket_notification_configuration(Bucket=bucket_name,
        #                                                            NotificationConfiguration=notification_configuration)
        #pprint(result)
        #pprint(s3.bucket_notification(bucket_name))

    def test_try_event_hooks(self):
        s3 = S3()
        deploy_lambda = Deploy_Lambda(run)
        file_name     = random_text('file_name') + '.txt'
        bucket_name = deploy_lambda.osbot_setup.s3_bucket_lambdas
        kwargs__create = dict(file_contents='some contents',
                              bucket=bucket_name,
                              key=file_name)
        kwargs__delete = dict(bucket=bucket_name,
                              key=file_name)
        s3.file_create_from_string(**kwargs__create)

        s3.file_delete            (**kwargs__delete)





