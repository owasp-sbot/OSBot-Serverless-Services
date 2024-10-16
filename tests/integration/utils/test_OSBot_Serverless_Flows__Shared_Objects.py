from unittest                                                            import TestCase
from tests.integration.fast_api_objs_for_tests                           import osbot_serverless__flows_local_stack, DEFAULT_TEST__AWS_ACCOUNT_ID
from osbot_serverless_flows.utils.OSBot_Serverless_Flows__Shared_Objects import osbot_serverless_flows__shared_objects


class test_OSBot_Serverless_Flows__Shared_Objects(TestCase):

    def test_s3_db_flows(self):
        assert osbot_serverless__flows_local_stack.local_stack.is_local_stack_configured_and_available() is True
        s3_db_flows = osbot_serverless_flows__shared_objects.s3_db_flows()

        assert s3_db_flows.s3_bucket() == F'osbot-serverless-flows-{DEFAULT_TEST__AWS_ACCOUNT_ID}-flows'
        assert s3_db_flows.bucket_exists()     is True
