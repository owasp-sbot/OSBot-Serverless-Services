from unittest                           import TestCase

import requests

from osbot_utils.utils.Env import load_dotenv, get_env

from tests.qa.test__live_lambda_server  import ENDPOINT_URL__QA_LAMBDA

class test__q__Playwright__Serverless(TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.endpoint_url = get_env('ENDPOINT_URL__QA_LAMBDA', ENDPOINT_URL__QA_LAMBDA)             # todo: refactor to something like TestCase__QA_Tests


    def test__ping(self):
        response = requests.get(f"{self.endpoint_url}/browser/ping")
        assert response.status_code == 200
        assert response.text        == '"pong"'

    def test__url_html(self):
        target_url = 'https://httpbin.org/get?answer=42'
        get_url    = f'{self.endpoint_url}/browser/url-html?url={target_url}'
        response   = requests.get(get_url)
        assert response.status_code == 200
        assert target_url in response.json().get('page_content')