import requests
from unittest               import TestCase
from osbot_utils.utils.Dev  import pprint
from osbot_utils.utils.Env  import get_env, load_dotenv

from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows

ENDPOINT_URL__QA_LAMBDA = 'https://serverless-flows.dev.aws.cyber-boardroom.com'

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
        assert response.json() == version__osbot_serverless_flows

    def test__hello(self):
        response = requests.get(f"{self.endpoint_url}/hello")
        assert response.status_code == 200
        assert response.json() == {'message': 'World!'}