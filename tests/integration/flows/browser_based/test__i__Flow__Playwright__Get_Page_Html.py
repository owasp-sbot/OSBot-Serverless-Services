from unittest                                                                   import TestCase

from osbot_utils.utils.Misc import list_set

from osbot_utils.helpers.flows.Flow import Flow

from osbot_utils.utils.Dev import pprint

from tests.integration.fast_api_objs_for_tests import ensure_browser_is_installed
from osbot_serverless_flows.flows.browser_based.Flow__Playwright__Get_Page_Html import Flow__Playwright__Get_Page_Html


class test__i__Flow__Playwright__Get_Page_Html(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ensure_browser_is_installed()
        cls.flow__get_page_html = Flow__Playwright__Get_Page_Html()

    def test_flow(self):
        with self.flow__get_page_html.flow() as _:
            assert type(_) is Flow
            assert _.flow_config.json() == { 'add_task_to_self'       : True,
                                             'log_to_console'         : False,
                                             'log_to_memory'          : True,
                                             'logging_enabled'        : True,
                                             'print_finished_message' : False,
                                             'print_logs'             : False,
                                             'print_none_return_value': False}
            assert _.execute_flow() == _
            assert list_set(_.data) == ['page_content']
            assert 'Google' in _.data.get('page_content')




    def test_run(self):

        flow_data = self.flow__get_page_html.run()
        page_content = flow_data.get('page_content')
        assert "<title>Google</title>" in page_content
        assert len(page_content) > 10000
