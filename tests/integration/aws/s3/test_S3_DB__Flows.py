from unittest                                                            import TestCase

from osbot_utils.utils.Dev import pprint

from tests.integration.fast_api_objs_for_tests                           import fast_api__local_stack
from osbot_local_stack.local_stack.Local_Stack                           import Local_Stack
from osbot_serverless_flows.Serverless_Flows__Server_Config              import DEFAULT__SERVERLESS_FLOWS__AWS_ACCOUNT_ID
from osbot_serverless_flows.Serverless_Flows__Shared_Objects             import serverless_flows__shared_objects
from osbot_serverless_flows.aws.s3.S3_DB__Flows                          import S3_DB__Flows


class test_S3_DB__Flows(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.local_stack = fast_api__local_stack
        cls.s3_db_flows = serverless_flows__shared_objects.s3_db_flows()

    def test__setup_class(self):
        assert type(self.local_stack)                                     is Local_Stack
        assert type(self.s3_db_flows)                                     == S3_DB__Flows
        assert self.local_stack.is_local_stack_configured_and_available() is True
        assert self.s3_db_flows.bucket_exists()                           is True
        assert self.s3_db_flows.s3_bucket    ()                           == f'serverless-flows-{DEFAULT__SERVERLESS_FLOWS__AWS_ACCOUNT_ID}-flows'