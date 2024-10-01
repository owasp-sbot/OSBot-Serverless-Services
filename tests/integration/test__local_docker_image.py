from unittest import TestCase

from osbot_aws.aws.lambda_.Lambda                   import Lambda
from osbot_aws.aws.session.Session__Kwargs__Lambda  import Session__Kwargs__Lambda


class test__local_docker_image(TestCase):
    @classmethod
    def setUpClass(cls):
        endpoint_url      = 'http://localhost:5002'
        cls.function_name = 'function'
        cls.session_kwargs__lambda = Session__Kwargs__Lambda(endpoint_url=endpoint_url).__locals__()

    def test__invoke_lambda(self):
        with Lambda(name=self.function_name, session_kwargs__lambda=self.session_kwargs__lambda) as _:
            assert _.invoke({}) == {'body': 'Hello from Docker Lambda!', 'statusCode': 200}
