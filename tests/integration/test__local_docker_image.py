from unittest import TestCase
import requests
from osbot_aws.testing.Temp__Random__AWS_Credentials import Temp__Random__AWS_Credentials

from osbot_aws.aws.lambda_.Lambda                   import Lambda
from osbot_aws.aws.session.Session__Kwargs__Lambda  import Session__Kwargs__Lambda


class test__local_docker_image(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.endpoint_url  = 'http://localhost:5002'
        cls.function_name = 'function'
        cls.session_kwargs__lambda = Session__Kwargs__Lambda(endpoint_url=cls.endpoint_url).__locals__()

    def test__invoke_lambda(self):
        with Temp__Random__AWS_Credentials():
            with Lambda(name=self.function_name, session_kwargs__lambda=self.session_kwargs__lambda) as _:
                assert _.invoke({}) == {'body': 'Hello from Docker Lambda!', 'statusCode': 200}

    def test__invoke_lambda__using_requests(self):
        invoke_url = f"{self.endpoint_url}/2015-03-31/functions/{self.function_name}/invocations"
        payload = {}
        response = requests.post(invoke_url, json=payload)
        assert response.status_code == 200
        assert response.json() == {'body': 'Hello from Docker Lambda!', 'statusCode': 200}

