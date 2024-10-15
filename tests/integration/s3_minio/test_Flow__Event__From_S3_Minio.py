import pytest
import requests
from osbot_aws.testing.TestCase__S3_Minio__Temp_S3_Bucket       import TestCase__S3_Minio__Temp_S3_Bucket
from osbot_utils.utils.Dev                                      import pprint
from osbot_serverless_flows.s3_minio.Flow__Event__From_S3_Minio import Flow__Event__From_S3_Minio

@pytest.mark.skip("needs rewriting to use LocalStack")
class test_Flow__Event__From_S3_Minio(TestCase__S3_Minio__Temp_S3_Bucket):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.flow_event_from_s3_minio = Flow__Event__From_S3_Minio()

    def test_target_method__in__fast_api(self):
        with self.flow_event_from_s3_minio as _:
            data = dict(answer=42)
            url = 'http://localhost:5005/dev/flow-testing-tasks'
            response = requests.post(url, json=data)
            assert response.status_code == 200
            pprint(response.json())

    #
    # def test_configure_minio_events(self):
    #
    #     with self.s3_db_base as _:
    #         target_bucket    = _.s3_bucket()
    #         notification_url = 'http://localhost:5005/dev/flow-testing-tasks'
    #         notification_configuration = {
    #             'TopicConfigurations': [],
    #             'QueueConfigurations': [],
    #             'LambdaFunctionConfigurations': [],
    #             'WebhookConfigurations': [
    #                 {
    #                     'Id': 'FastAPIWebhook',  # A unique ID for the webhook
    #                     'Events': ['s3:ObjectCreated:*'],  # Trigger on all object created events
    #                     'Destination': {
    #                         'Endpoint': notification_url,  # Your FastAPI webhook
    #                         'HttpMethod': 'POST',
    #                         'Authentication': {
    #                             'Type': 'None',  # No authentication for this example; you can configure this if needed
    #                         },
    #                     }
    #                 }
    #             ]
    #         }
    #         #pprint(_.s3().buckets())
    #         s3_client = _.s3().client()
    #         pprint(target_bucket)
    #         result = s3_client.put_bucket_notification_configuration(
    #             Bucket= target_bucket,
    #             NotificationConfiguration=notification_configuration
    #         )
    #         pprint(result)

    def test_prefect_server(self):
        from osbot_aws.aws.s3.S3 import S3
        kwargs = dict(aws_access_key_id     = "localstack"           ,
                      aws_secret_access_key = "localstack"           ,
                      endpoint_url          = "http://localhost:4566",
                      region_name           = "eu-west-1"            )

        # S3 EXAMPLE

        #bucket_name = 'an-bucket'
        #region_name = "eu-west-1"
        #file_contents = random_text('hello world')
        #s3 = S3(session_kwargs__s3= Session__Kwargs__S3(**kwargs))
        # result= s3.bucket_create(bucket_name, region_name)
        # pprint(result)
        #pprint(s3.buckets())
        # pprint(s3.file_create_from_string(bucket=bucket_name, key='test.txt', file_contents=file_contents))
        # pprint(s3.find_files(bucket_name))
        # with print_duration():
        #     pprint(s3.file_contents(bucket_name, 'test.txt'))
        #     assert s3.file_contents(bucket_name, 'test.txt') == file_contents


        # # Lambda EXAMPLE
        # lambda_name = 'an_lambda'
        # with Lambda()