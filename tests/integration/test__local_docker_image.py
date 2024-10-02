from unittest import TestCase

import pytest
import requests
from osbot_utils.utils.Env import get_env

from osbot_aws.testing.Temp__Random__AWS_Credentials import Temp__Random__AWS_Credentials

from osbot_aws.aws.lambda_.Lambda                   import Lambda
from osbot_aws.aws.session.Session__Kwargs__Lambda  import Session__Kwargs__Lambda


class test__local_docker_image(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.endpoint_url  = get_env('TARGET_SERVER')
        cls.function_name = 'function'
        cls.session_kwargs__lambda = Session__Kwargs__Lambda(endpoint_url=cls.endpoint_url).__locals__()

    def test__invoke_lambda(self):
        with Temp__Random__AWS_Credentials():
            with Lambda(name=self.function_name, session_kwargs__lambda=self.session_kwargs__lambda) as _:
                assert _.invoke({}) == {'body': 'Hello from Docker Lambda!', 'statusCode': 200}

    def test__invoke_lambda__using_requests(self):
        # The local endpoint to invoke the Lambda function using HTTP
        invoke_url = f"{self.endpoint_url}/2015-03-31/functions/{self.function_name}/invocations"

        # Define the payload you want to send to the Lambda function
        payload = {}

        # Send a POST request to the local Lambda endpoint
        response = requests.post(invoke_url, json=payload)

        # Check the response from the Lambda function
        assert response.status_code == 200
        assert response.json() == {'body': 'Hello from Docker Lambda!', 'statusCode': 200}

