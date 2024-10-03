from unittest                                                   import TestCase

from playwright.async_api import Playwright

from osbot_utils.utils.Threads import async_invoke_in_new_loop

from osbot_utils.utils.Env                                      import in_github_action
from osbot_utils.utils.Files                                    import file_name, file_exists, folder_exists, folder_name
from osbot_serverless_flows.playwright.Playwright__Serverless   import Playwright__Serverless
from osbot_utils.utils.Dev                                      import pprint


class test_Playwright__Serverless(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright__serverless = Playwright__Serverless()

    def test__init__(self):
        with self.playwright__serverless as _:
            expected_locals = dict(playwright_cli=_.playwright_cli)
            assert self.playwright__serverless.__locals__() == expected_locals

    def test_chrome_path(self):
        with self.playwright__serverless as _:
            chrome_path = _.chrome_path()
            if in_github_action():
                assert chrome_path.endswith('chrome') is True
            else:
                assert file_exists(chrome_path)
                assert file_name(chrome_path) == 'Chromium'

    def test_playwright(self):
        with self.playwright__serverless as _:
            assert type(_.playwright()) is Playwright
