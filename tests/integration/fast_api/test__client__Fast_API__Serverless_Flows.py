from unittest                                                   import TestCase
from osbot_serverless_flows.fast_api.routes.Routes__Debug       import ROUTES__EXPECTED_PATHS__DEBUG
from osbot_serverless_flows.fast_api.routes.Routes__Dev         import ROUTES__EXPECTED_PATHS__DEV
from osbot_serverless_flows.fast_api.routes.Routes__GSuite      import ROUTES__EXPECTED_PATHS__GSUITE
from osbot_serverless_flows.fast_api.Fast_API__Serverless_Flows import Fast_API__Serverless_Flows
from osbot_serverless_flows.fast_api.routes.Routes__Browser     import ROUTES__EXPECTED_PATHS__BROWSER
from osbot_serverless_flows.fast_api.routes.Routes__Info        import ROUTES__EXPECTED_PATHS__INFO
from osbot_serverless_flows.utils.Version                       import version__osbot_serverless_flows
from tests.integration.fast_api_objs_for_tests                  import fast_api__serverless_flows, client__serverless_flows

ROUTES__EXPECTED_PATHS__FAST_API = [ '/'              ,
                                     '/config/status' ,
                                     '/config/version']

ROUTES__EXPECTED_PATHS = sorted([ ] +
                                ROUTES__EXPECTED_PATHS__BROWSER  +
                                ROUTES__EXPECTED_PATHS__DEBUG    +
                                ROUTES__EXPECTED_PATHS__DEV      +
                                ROUTES__EXPECTED_PATHS__INFO     +
                                ROUTES__EXPECTED_PATHS__FAST_API +
                                ROUTES__EXPECTED_PATHS__GSUITE   )

class test__client__Fast_API__Serverless_Flows(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fast_api = fast_api__serverless_flows
        cls.client   = client__serverless_flows

    def test__setUp_Class(self):
        assert type(self.fast_api) is Fast_API__Serverless_Flows

    def test_setup(self):
        assert self.fast_api.routes_paths() != []

    def test_setup__prefect_cloud(self):
        with self.fast_api.flow_events_to_prefect_server().prefect_cloud_api.prefect_rest_api as _:
            if _.prefect_is_using_local_server():
                assert _.prefect_api_url()       == 'http://localhost:4200/api'
                assert _.prefect_is_server_online() is True
            else:
                assert _.prefect_api_url().startswith('https://api.prefect.cloud/api/accounts') is True
                assert _.prefect_is_server_online() is True

        assert self.fast_api.prefect_enabled is True

    def test_routes_paths(self):
        assert self.fast_api.routes_paths() == ROUTES__EXPECTED_PATHS

    def test__route__root(self):
        response = self.client.get('/', follow_redirects=False)
        assert response.status_code             == 307
        assert response.headers.get('location') == '/docs'

    def test__route__ping(self):
        response = self.client.get('/info/ping')
        assert response.status_code == 200
        assert response.json()      == {"pong": "42"}

    def test__route__version(self):
        response = self.client.get('/info/version')
        assert response.status_code == 200
        assert response.json()      == {"version": version__osbot_serverless_flows }


