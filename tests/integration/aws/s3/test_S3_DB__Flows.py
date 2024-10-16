from unittest import TestCase

from tests.integration.fast_api_objs_for_tests                           import osbot_serverless__flows_local_stack, DEFAULT_TEST__AWS_ACCOUNT_ID
from osbot_serverless_flows.utils.OSBot_Serverless_Flows__Shared_Objects import osbot_serverless_flows__shared_objects

from osbot_utils.utils.Dev import pprint

from osbot_local_stack.testing.TestCase__Local_Stack import TestCase__Local_Stack
from osbot_serverless_flows.aws.s3.S3_DB__Flows import S3_DB__Flows


class test_S3_DB__Flows(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.local_stack = osbot_serverless__flows_local_stack.local_stack
        cls.s3_db_flows = osbot_serverless_flows__shared_objects.s3_db_flows()

    def test__setup_class(self):
        assert self.s3_db_flows.bucket_exists() is True
        assert self.s3_db_flows.s3_bucket    () == f'osbot-serverless-flows-{DEFAULT_TEST__AWS_ACCOUNT_ID}-flows'