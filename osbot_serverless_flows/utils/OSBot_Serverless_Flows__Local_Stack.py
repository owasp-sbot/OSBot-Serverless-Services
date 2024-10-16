from osbot_aws.testing.Temp__Random__AWS_Credentials import Temp_AWS_Credentials

from osbot_local_stack.local_stack.Local_Stack import Local_Stack
from osbot_utils.base_classes.Type_Safe import Type_Safe


class OSBot_Serverless_Flows__Local_Stack(Type_Safe):
    local_stack         : Local_Stack
    temp_asw_credentials: Temp_AWS_Credentials

    def activate(self):
        self.temp_asw_credentials.set_vars()
        self.local_stack.activate         ()
        return self