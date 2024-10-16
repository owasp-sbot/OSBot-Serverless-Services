from unittest                                                import TestCase
from integration.fast_api_objs_for_tests                     import fast_api__local_stack
from osbot_serverless_flows.Serverless_Flows__Server_Config  import DEFAULT__SERVERLESS_FLOWS__AWS_ACCOUNT_ID
from osbot_serverless_flows.Serverless_Flows__Shared_Objects import serverless_flows__shared_objects

class test_Serverless_Flows__Shared_Objects(TestCase):

    def test_s3_db_flows(self):
        assert fast_api__local_stack.is_local_stack_configured_and_available() is True
        s3_db_flows = serverless_flows__shared_objects.s3_db_flows()

        assert s3_db_flows.s3_bucket()      == F'serverless-flows-{DEFAULT__SERVERLESS_FLOWS__AWS_ACCOUNT_ID}-flows'
        assert s3_db_flows.bucket_exists()  is True
