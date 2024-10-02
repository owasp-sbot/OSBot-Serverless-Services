from unittest import TestCase

import requests
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Env import get_env, load_dotenv
from osbot_utils.utils.Http import GET

from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows

ENDPOINT_URL__QA_LAMBDA = 'https://a4sbatx723cfs7tw3kbiifv37q0evpcp.lambda-url.eu-west-1.on.aws'

class test__live_lambda_server(TestCase):

    def setUp(self):
        load_dotenv()
        self.endpoint_url = get_env('ENDPOINT_URL__QA_LAMBDA', ENDPOINT_URL__QA_LAMBDA)


    def test__ping(self):
        response = requests.get(f"{self.endpoint_url}/ping")
        assert response.status_code == 200
        assert response.json() == {'pong': '42'}

    def test__docs(self):
        response = requests.get(f"{self.endpoint_url}/docs")
        assert response.status_code == 200
        assert "Swagger UI" in response.text

    def test__openapi(self):
        response = requests.get(f"{self.endpoint_url}/openapi.json")
        assert response.status_code == 200
        assert "openapi" in response.json()

    def test__version(self):
        response = requests.get(f"{self.endpoint_url}/version")
        assert response.status_code == 200
        pprint(response.json())