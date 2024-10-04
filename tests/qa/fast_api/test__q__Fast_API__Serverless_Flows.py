import requests
from unittest                                   import TestCase
from osbot_fast_api.utils.Version               import version__osbot_fast_api
from osbot_serverless_flows.utils.Version       import version__osbot_serverless_flows
from osbot_utils.utils.Env                      import get_env, load_dotenv

from tests.qa.test__live_lambda_server          import ENDPOINT_URL__QA_LAMBDA

class test__q__Fast_API__Serverless_Flows(TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.endpoint_url = get_env('ENDPOINT_URL__QA_LAMBDA', ENDPOINT_URL__QA_LAMBDA)             # todo: refactor to something like TestCase__QA_Tests

    def test__config__status (self): assert requests.get(f"{self.endpoint_url}/config/status" ).json() == {'status' : 'ok'                            }
    def test__config__version(self): assert requests.get(f"{self.endpoint_url}/config/version").json() == {'version': version__osbot_fast_api         }
    def test__info__ping     (self): assert requests.get(f"{self.endpoint_url}/info/ping"     ).json() == {'pong'   : '42'                            }
    def test__info__version  (self): assert requests.get(f"{self.endpoint_url}/info/version"  ).json() == {'version': version__osbot_serverless_flows }

    def test__docs(self):
        response = requests.get(f"{self.endpoint_url}/docs")
        assert response.status_code == 200
        assert "Swagger UI" in response.text

    def test__openapi(self):
        response = requests.get(f"{self.endpoint_url}/openapi.json")
        assert response.status_code == 200
        assert "openapi" in response.json()