from unittest                                    import TestCase

from fastapi                                                    import FastAPI
from osbot_fast_api.utils.Fast_API_Server                       import Fast_API_Server
from osbot_fast_api.utils.Version                               import version__osbot_fast_api
from osbot_utils.utils.Misc                                     import list_set
from tests.integration.fast_api_objs_for_tests                  import fast_api__serverless_flows
from osbot_serverless_flows.fast_api.Fast_API__Serverless_Flows import Fast_API__Serverless_Flows
from osbot_serverless_flows.utils.Version                       import version__osbot_serverless_flows
from osbot_utils.context_managers.print_duration                import print_duration


class test__http__Fast_API__Serverless_Flows(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        with print_duration():
            cls.fast_api__serverless_flows      = fast_api__serverless_flows
            cls.fast_api__serverless_flows__app = fast_api__serverless_flows.app()
            cls.fast_api_server                 = Fast_API_Server(app=cls.fast_api__serverless_flows__app)
            cls.fast_api_server.start()
            assert cls.fast_api_server.is_port_open() is True

    @classmethod
    def tearDownClass(cls) -> None:
        cls.fast_api_server.stop()
        assert cls.fast_api_server.is_port_open() is False

    def test__setUpClass(self):
        assert type(self.fast_api__serverless_flows     ) is Fast_API__Serverless_Flows
        assert type(self.fast_api__serverless_flows__app) is FastAPI
        assert type(self.fast_api_server                ) is Fast_API_Server

    def test_version(self):
        assert self.fast_api_server.requests_get('/config/version').json() == {'version': version__osbot_fast_api         }
        assert self.fast_api_server.requests_get('/info/version'  ).json() == {'version': version__osbot_serverless_flows }

    def test__dev__flow_testing_tasks(self):
        path        = 'dev/flow-testing-tasks'
        data        = {'answer': 42}
        response    = self.fast_api_server.requests_post(path, data)
        flow_run_id = response.headers.get('flow-run-id')
        assert list_set(response.headers) == ['content-length', 'content-type', 'date',
                                              'fast-api-request-id', 'flow-run-id', 'server']

        assert response.json() == {'flow_result': f'flow completed: {flow_run_id} ',
                                    'post_data' : {'answer': 42                 }}

