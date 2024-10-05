import requests

from osbot_utils.utils.Env import get_env

from osbot_utils.base_classes.Type_Safe import Type_Safe

ENV_NAME__PREFECT_CLOUD__API_KEY      = 'PREFECT_CLOUD__API_KEY'
ENV_NAME__PREFECT_CLOUD__ACCOUNT_ID   = 'PREFECT_CLOUD__ACCOUNT_ID'
ENV_NAME__PREFECT_CLOUD__WORKSPACE_ID = 'PREFECT_CLOUD__WORKSPACE_ID'


class Prefect__Publish_To_Cloud(Type_Safe):
    Prefect__Account_id : str

    def api_key(self):
        return get_env(ENV_NAME__PREFECT_CLOUD__API_KEY)

    def account_id(self):
        return get_env(ENV_NAME__PREFECT_CLOUD__ACCOUNT_ID)

    def workspace_id(self):
        return get_env(ENV_NAME__PREFECT_CLOUD__WORKSPACE_ID)

    def prefect_api_url(self):
        return f"https://app.prefect.cloud/account/{self.account_id()}/workspace/{self.workspace_id()}/flows"

    def make_request(self):
        return

        data = {
            "sort": "CREATED_DESC",
            "limit": 5,
            "artifacts": {
                "key": {
                    "exists_": True
                }
            }
        }

        headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}
        endpoint = f"{PREFECT_API_URL}/artifacts/filter"

        response = requests.post(endpoint, headers=headers, json=data)
        assert response.status_code == 200
        for artifact in response.json():
            print(artifact)
