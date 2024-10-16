from unittest                                                           import TestCase

from osbot_serverless_flows.Serverless_Flows__Server_Config import serverless_flows__server_config, \
    DEFAULT__SERVERLESS_FLOWS__AWS_ACCOUNT_ID, ENV_NAME__SERVERLESS_FLOWS__USE_LOCAL_STACK
from osbot_utils.testing.Temp_Env_Vars                      import Temp_Env_Vars
from osbot_utils.utils.Objects                              import __


class test_OSBot_Serverless_Flows__Server_Config(TestCase):

    def test_setup(self):
        original_values = serverless_flows__server_config.obj()

        def reset_values():
            serverless_flows__server_config.reset()
            assert serverless_flows__server_config.obj() == __(aws_account_id=DEFAULT__SERVERLESS_FLOWS__AWS_ACCOUNT_ID, use_local_stack=False)
            serverless_flows__server_config.setup()
            assert serverless_flows__server_config.obj() == original_values

        with Temp_Env_Vars(env_vars={'AWS_ACCOUNT_ID': '1234567890'}):
            assert serverless_flows__server_config.setup().aws_account_id == '1234567890'
        reset_values()

        with Temp_Env_Vars(env_vars={ENV_NAME__SERVERLESS_FLOWS__USE_LOCAL_STACK: 'True'}):
            assert serverless_flows__server_config.setup().use_local_stack == True
        reset_values()

        with Temp_Env_Vars(env_vars={ENV_NAME__SERVERLESS_FLOWS__USE_LOCAL_STACK: 'False'}):
            assert serverless_flows__server_config.setup().use_local_stack == original_values.use_local_stack
        reset_values()