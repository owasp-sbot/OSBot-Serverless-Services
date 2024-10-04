from unittest import TestCase

from tests.integration.fast_api_objs_for_tests import ensure_browser_is_installed
from osbot_serverless_flows.fast_api.routes.Routes__Browser import Routes__Browser


class test__u__Routes_Browser(TestCase):

    @classmethod
    def setUpClass(cls):
        ensure_browser_is_installed()
        cls.routes_browser = Routes__Browser()

    def test_url_html(self):
        url = 'https://httpbin.org/get'
        assert url in self.routes_browser.url_html().get('page_content')
