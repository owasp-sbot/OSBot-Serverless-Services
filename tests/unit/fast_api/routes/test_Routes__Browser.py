from unittest import TestCase

from osbot_serverless_flows.fast_api.routes.Routes__Browser import Routes__Browser


class test_Routes_Browser(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.routes_browser = Routes__Browser()

    def test_url_html(self):
        url = 'https://httpbin.org/get'
        assert url in self.routes_browser.url_html().get('page_content')
