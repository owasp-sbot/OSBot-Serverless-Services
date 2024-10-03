from unittest import TestCase

from osbot_utils.utils.Files import file_name, file_exists

from osbot_utils.utils.Dev import pprint

from osbot_serverless_flows.playwright.Playwright__Serverless import Playwright__Serverless


class test_Playwright__Serverless(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.playwright__serverless = Playwright__Serverless()

    def test__init__(self):
        assert self.playwright__serverless.__locals__() == {}

    def test_chrome_path(self):
        with self.playwright__serverless as _:
            chrome_path = _.chrome_path()
            print("****** Chrome Path ******")
            pprint(chrome_path)
            assert file_exists(chrome_path)
            assert file_name(chrome_path) == 'Chromium'
