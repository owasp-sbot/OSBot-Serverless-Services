from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from osbot_serverless_flows.flows.browser_based.Flow__Playwright__Get_Page_Html import Flow__Playwright__Get_Page_Html


class test_Flow__Playwright__Get_Page_Html(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.flow__get_page_html = Flow__Playwright__Get_Page_Html()

    def test_run(self):
        flow_data = self.flow__get_page_html.run()
        page_content = flow_data.get('page_content')
        assert "<title>Google</title>" in page_content
        assert len(page_content) > 10000
