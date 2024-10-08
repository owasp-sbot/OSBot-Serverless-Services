from unittest                           import TestCase

import requests
from osbot_utils.utils.Dev import pprint

from osbot_utils.utils.Env import load_dotenv, get_env
from osbot_utils.utils.Misc import url_encode

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
        get_url    = f'{self.endpoint_url}/browser/url-html?url={url_encode(target_url)}'
        response   = requests.get(get_url)
        assert response.status_code == 200
        assert target_url in response.json().get('page_content')

    def test__url_screenshot(self):
        target_url = 'https://httpbin.org/get?answer=42'
        get_url = f'{self.endpoint_url}/browser/url-screenshot?url={url_encode(target_url)}'
        response = requests.get(get_url)
        assert response.status_code == 200
        assert len(response.json().get('screenshot_base64')) > 10000

    def test__url_pdf(self):
        target_url = 'https://httpbin.org/get?answer=42'
        get_url = f'{self.endpoint_url}/browser/url-pdf?url={url_encode(target_url)}'
        response = requests.get(get_url)
        assert response.status_code == 200
        assert len(response.json().get('pdf_base64')) > 10000