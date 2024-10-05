from unittest import TestCase

from osbot_utils.utils.Misc import list_set

from osbot_utils.utils.Dev import pprint

from osbot_serverless_flows.observability.prefect.Prefect__Cloud_API import Prefect__Cloud_API
from osbot_utils.utils.Env import load_dotenv


class test_Prefect__Cloud_API(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.prefect_cloud_api = Prefect__Cloud_API()

    def test_flows(self):
        response    = self.prefect_cloud_api.flows()
        status_code = response.status_code
        flows       = response.json()
        assert status_code == 200
        for flow in flows:
            assert list_set(flow) == ['created', 'id', 'labels', 'name', 'tags', 'updated']
