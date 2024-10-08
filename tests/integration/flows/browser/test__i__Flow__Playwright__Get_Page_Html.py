from unittest                                                                   import TestCase

import pytest
from osbot_playwright._extra_methdos_osbot import in_github_actions
from osbot_utils.utils.Env import not_in_github_action, in_github_action

from osbot_prefect.flows.Flow_Events__To__Prefect_Server import Flow_Events__To__Prefect_Server
from osbot_utils.utils.Misc import list_set

from osbot_utils.helpers.flows.Flow import Flow

from osbot_utils.utils.Dev import pprint

from tests.integration.fast_api_objs_for_tests import ensure_browser_is_installed
from osbot_serverless_flows.flows.browser.Flow__Playwright__Get_Page_Html import Flow__Playwright__Get_Page_Html


class test__i__Flow__Playwright__Get_Page_Html(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ensure_browser_is_installed()
        cls.flow__get_page_html = Flow__Playwright__Get_Page_Html()

    def test_flow_playwright__get_page_html(self):
        with Flow_Events__To__Prefect_Server():
            with self.flow__get_page_html.flow_playwright__get_page_html() as _:
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



    # todo: figure out why this hangs when executed after the test above
    # def test_run(self):
    #     # if in_github_action():
    #     #     pytest.mark.skip("Test works locally but was hanging in GH Actions")
    #     with Flow_Events__To__Prefect_Server():
    #         flow_data = self.flow__get_page_html.run()
    #         page_content = flow_data.get('page_content')
    #         assert "<title>Google</title>" in page_content
    #         assert len(page_content) > 10000
