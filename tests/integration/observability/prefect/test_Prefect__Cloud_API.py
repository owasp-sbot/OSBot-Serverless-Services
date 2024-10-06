from unittest                                                           import TestCase

from osbot_serverless_flows.observability.prefect.Prefect__Rest_API     import ENV_NAME__PREFECT_TARGET_SERVER
from osbot_utils.utils.Lists                                            import list_in_list
from osbot_utils.utils.Misc                                             import list_set
from osbot_serverless_flows.observability.prefect.Prefect__Cloud_API    import Prefect__Cloud_API
from osbot_utils.utils.Env                                              import load_dotenv, get_env

class test_Prefect__Cloud_API(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.prefect_cloud_api = Prefect__Cloud_API()

    def test_confirm_local_docker(self):
        assert get_env(ENV_NAME__PREFECT_TARGET_SERVER) == 'http://localhost:4200/api'

    def test_flows(self):
        flows    = self.prefect_cloud_api.flows()
        for flow in flows:
            assert list_in_list(["created", "id", "tags", "updated"], list_set(flow)) is True

    def test_flow(self):
        with self.prefect_cloud_api as _:
            flows_ids = _.flows_ids()
            if flows_ids:
                flow_id   = flows_ids.pop()
                flow      = self.prefect_cloud_api.flow(flow_id=flow_id)
                assert list_in_list(["created", "id", "tags", "updated"], list_set(flow)) is True