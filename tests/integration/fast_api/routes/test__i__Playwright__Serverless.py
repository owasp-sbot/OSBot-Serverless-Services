from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from integration.fast_api_objs_for_tests import client__serverless_flows


class test__i__Playwright__Serverless(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client   = client__serverless_flows

    def test__route__ping(self):
        target_url   = 'https://httpbin.org/get?answer=42'
        get_url      = f'/browser/url-html?url={target_url}'
        response = self.client.get(get_url)
        assert response.status_code == 200
        page_content =  response.json().get('page_content')
        assert target_url in page_content
