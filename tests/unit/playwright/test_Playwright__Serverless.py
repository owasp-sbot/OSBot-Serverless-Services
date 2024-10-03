from unittest                                                   import TestCase

from playwright.async_api import Playwright, Browser

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

    def test_1__browser__install(self):                                         # (first test to be executed) make sure that the browser is installed
        with self.playwright__serverless as _:
            assert _.browser__install() is True

    def test_browser(self):
        with self.playwright__serverless as _:
            browser = async_invoke_in_new_loop(_.browser())
            assert type(browser) is Browser

    def test_browser__exists(self):
        with self.playwright__serverless as _:
            assert _.browser__exists() is True

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
            playwright = async_invoke_in_new_loop(_.playwright())
            assert type(playwright) is Playwright

    # ----------

    def test_run_playwright_in_pytest(self):
        from osbot_utils.utils.Threads                       import async_invoke_in_new_loop
        from osbot_utils.utils.Misc                          import bytes_to_base64
        from playwright.async_api                            import async_playwright
        from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
        playwright_cli = Playwright_CLI()
        chrome_path    = playwright_cli.executable_path__chrome()
        pprint(chrome_path)

        async def get_screenshot(url):

            context = await async_playwright().start()
            launch_kwargs = dict(args=["--disable-gpu", "--single-process"],
                                 executable_path=chrome_path)
            browser = await context.chromium.launch(**launch_kwargs)
            return browser

            page = await browser.new_page()
            await page.goto(url)

            screenshot = await page.screenshot(full_page=True)
            return bytes_to_base64(screenshot)

        result = async_invoke_in_new_loop(get_screenshot("https://www.google.com/404"))
        pprint(result)

