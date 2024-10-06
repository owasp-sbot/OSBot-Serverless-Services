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
        flows    = self.prefect_cloud_api.flows()
        for flow in flows:
            assert list_set(flow) == ['created', 'id', 'labels', 'name', 'tags', 'updated']

    def test_flow(self):
        with self.prefect_cloud_api as _:
            flows_ids = _.flows_ids()
            flow_id   = flows_ids.pop()
            flow      = self.prefect_cloud_api.flow(flow_id=flow_id)
            assert list_set(flow) == ['created', 'id', 'labels', 'name', 'tags', 'updated']