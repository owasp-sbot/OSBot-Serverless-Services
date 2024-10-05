from unittest import TestCase

from osbot_serverless_flows.observability.prefect.Prefect__Cloud_API import Prefect__Cloud_API
from osbot_utils.utils.Env import load_dotenv


class test_Prefect__Cloud_API(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.prefect_cloud_api = Prefect__Cloud_API()

    def test_make_request(self):
        response = self.prefect_cloud_api.make_request()
        from osbot_utils.utils.Dev import pprint
        assert response.status_code == 200
