from unittest import TestCase

import requests
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Http import GET


class test__live_lambda_server(TestCase):

    def test__invoke_url(self):
        function_url = 'https://a4sbatx723cfs7tw3kbiifv37q0evpcp.lambda-url.eu-west-1.on.aws'
        response     = requests.get(function_url)
        assert response.status_code == 200
        assert response.text        == 'Hello from Docker Lambda!'