from unittest                           import TestCase

import requests
from osbot_utils.utils.Dev import pprint

from osbot_utils.utils.Env import load_dotenv, get_env
from tests.qa.for_qa_tests import qa__endpoint_url


class test__q__Playwright__Serverless(TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.endpoint_url = qa__endpoint_url

    def test_install_browser(self):
        get_url                = f'{self.endpoint_url}/browser/install-browser'
        response               = requests.get(get_url)
        assert response.json() == {'status': True}


    def test__url_html(self):
        target_url = 'https://httpbin.org/get?answer=42'
        get_url    = f'{self.endpoint_url}/browser/url-html?url={target_url}'
        response   = requests.get(get_url)
        assert response.status_code == 200
        assert target_url in response.json().get('page_content')