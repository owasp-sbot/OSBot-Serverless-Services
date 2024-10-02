from unittest import TestCase

import requests
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Http import GET

from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows


class test__live_lambda_server(TestCase):

    def test__invoke_url(self):
        expected_message = f'Hello from main code Lambda! | version: {version__osbot_serverless_flows}'
        function_url     = 'https://a4sbatx723cfs7tw3kbiifv37q0evpcp.lambda-url.eu-west-1.on.aws'
        response         = requests.get(function_url)
        assert response.status_code == 200
        assert response.text        == expected_message