from unittest                                                    import TestCase
from osbot_serverless_flows.playwright.Playwright__Install_Check import Playwright__Install_Check


class test_Playwright__Install_Check(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.playwright_chrome_setup = Playwright__Install_Check()

    def test_browser__install_check(self):
        with self.playwright_chrome_setup as _:
            result = _.browser__install_check()
            assert result == { 'chrome__dependencies_validated': True ,
                               'chrome__installation_complete' : True ,
                               'ffmpeg__installation_complete' : True ,
                               'installed_ok'                  : True }
