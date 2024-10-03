from unittest                                                       import TestCase
from osbot_utils.utils.Files                                        import bytes_to_file, file_exists, file_delete, file_bytes
from osbot_utils.utils.Misc                                         import base64_to_bytes
from osbot_serverless_flows.utils._for_osbot_aws.Http__Remote_Shell import Http__Remote_Shell

class test__remote_shell_docker(TestCase):

    def setUp(self):
        self.port  = 5002
        target_url = f'http://localhost:{self.port}/debug/lambda-shell'
        self.shell = Http__Remote_Shell(target_url=target_url)

    def test_0_lambda_shell_setup(self):
        assert self.shell.ping() == 'pong'

    def test_1_check_osbot_utils_version(self):

        def check_osbot_utils_version():
            from osbot_utils.utils.Version import Version
            return Version().value()

        assert self.shell.function(check_osbot_utils_version) == 'v1.47.0'


    def test_2_playwright__install_chrome(self):
        def playwright__install_chrome():
            from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
            playwright_cli = Playwright_CLI()
            result         = playwright_cli.install__chrome()
            return f'{result}'

        assert self.shell.function(playwright__install_chrome) == 'True'

    def test_3_playwright__new_page(self):

        def playwright__new_page():
            from osbot_utils.utils.Threads import async_invoke_in_new_loop
            from playwright.async_api      import async_playwright

            async def run_in_new_loop():
                context = await async_playwright().start()
                browser = await context.chromium.launch(args=["--disable-gpu", "--single-process"])
                page    = await browser.new_page()
                return f'{page}'

            return async_invoke_in_new_loop(run_in_new_loop())

        assert self.shell.function(playwright__new_page) == "<Page url='about:blank'>"

    def test_4_playwright__open_page(self):

        def playwright__open_page():
            from osbot_utils.utils.Threads import async_invoke_in_new_loop
            from playwright.async_api      import async_playwright

            async def run_in_new_loop(url):
                context = await async_playwright().start()
                browser = await context.chromium.launch(args=["--disable-gpu", "--single-process"])
                page    = await browser.new_page()
                await page.goto(url)
                return f'{page}'

            target_url = 'https://www.google.com/404'
            return async_invoke_in_new_loop(run_in_new_loop(target_url))

        assert self.shell.function(playwright__open_page) == "<Page url='https://www.google.com/404'>"


    def test_5_playwright__page_screenshot(self):

        def playwright__page_screenshot():
            from osbot_utils.utils.Threads import async_invoke_in_new_loop
            from playwright.async_api      import async_playwright
            from osbot_utils.utils.Misc    import bytes_to_base64

            async def run_in_new_loop(url):
                context = await async_playwright().start()
                browser = await context.chromium.launch(args=["--disable-gpu", "--single-process"])
                page    = await browser.new_page()
                await page.goto(url)
                screenshot = await page.screenshot(full_page=True)

                return bytes_to_base64(screenshot)

            target_url = 'https://www.google.com/404'
            target_url = 'https://dev.cyber-boardroom.com/docs'
            return async_invoke_in_new_loop(run_in_new_loop(target_url))

        screenshot_base64 = self.shell.function(playwright__page_screenshot)
        screenshot_bytes  = base64_to_bytes(screenshot_base64)
        screenshot_file   = bytes_to_file(bytes=screenshot_bytes, extension='.png')
        assert len        (screenshot_base64) > 8000
        assert type       (screenshot_bytes ) is bytes
        assert file_exists(screenshot_file  ) is True
        assert file_bytes (screenshot_file  ) == screenshot_bytes
        assert file_delete(screenshot_file  ) is True



