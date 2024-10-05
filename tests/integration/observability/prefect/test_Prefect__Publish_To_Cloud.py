from unittest import TestCase

from osbot_utils.utils.Env import load_dotenv, get_env

from osbot_serverless_flows.observability.prefect.Prefect__Publish_To_Cloud import Prefect__Publish_To_Cloud, \
    ENV_NAME__PREFECT_CLOUD__API_KEY


class test_Prefect__Publish_To_Cloud(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.prefect_publish = Prefect__Publish_To_Cloud()

    def test_api_key(self):
        assert self.prefect_publish.api_key() == get_env(ENV_NAME__PREFECT_CLOUD__API_KEY)

    def test_prefect_api_url(self):
        account_id   = self.prefect_publish.account_id()
        workspace_id = self.prefect_publish.workspace_id()
        expected_url = f"https://app.prefect.cloud/account/{account_id}/workspace/{workspace_id}/flows"
        assert self.prefect_publish.prefect_api_url() == expected_url
