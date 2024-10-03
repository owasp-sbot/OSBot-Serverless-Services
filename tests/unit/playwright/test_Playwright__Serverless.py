from unittest                                                   import TestCase
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
            print("****** Chrome Path ******")
            pprint(chrome_path)
            if in_github_action():
                assert folder_exists(chrome_path)
                assert folder_name(chrome_path) == 'chrome'
            else:
                assert file_exists(chrome_path)
                assert file_name(chrome_path) == 'Chromium'
