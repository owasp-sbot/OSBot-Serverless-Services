from unittest                                                       import TestCase
from osbot_utils.utils.Misc                                         import base64_to_bytes
from osbot_serverless_flows.utils._for_osbot_aws.Http__Remote_Shell import Http__Remote_Shell


class test_remote_shell_lambda(TestCase):

    def setUp(self):
        self.port  = 5002
        target_url = f'https://serverless-flows.dev.aws.cyber-boardroom.com/debug/lambda-shell'
        self.shell = Http__Remote_Shell(target_url=target_url)

    def test_0_lambda_shell_setup(self):
        assert self.shell.ping() == 'pong'


    def test_1_ping(self):
        def return_value():
            return 'here....'
        assert self.shell.function(return_value) == 'here....'

    def test_2_playwright__install_chrome(self):
        def playwright__install_chrome():
            from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
            playwright_cli = Playwright_CLI()
            result = playwright_cli.install__chrome()
            return f'{result}'

        install_result           = self.shell.function(playwright__install_chrome)
        assert install_result   == 'True'

    def test_3_run_playwright__page_screenshot(self):

        def playwright__page_screenshot():
            from osbot_utils.utils.Threads import async_invoke_in_new_loop
            from osbot_utils.utils.Misc    import bytes_to_base64
            from playwright.async_api      import async_playwright

            async def get_screenshot(url):
                context = await async_playwright().start()
                browser = await context.chromium.launch(args=["--disable-gpu", "--single-process"])
                page    = await browser.new_page()
                await page.goto               (url)

                screenshot = await page.screenshot(full_page=True)
                return bytes_to_base64(screenshot)

            target_url = "https://www.google.com/404"
            return async_invoke_in_new_loop(get_screenshot(url=target_url))

        screenshot_base64 = self.shell.function(playwright__page_screenshot)
        screenshot_bytes  = base64_to_bytes(screenshot_base64)

        assert len(screenshot_base64)   > 8000
        assert type(screenshot_bytes)   is bytes

    def test_4_check_new_osbot_threading_async_execution(self):                 # test running on my local dev laptop

        def execute_in_lambda():                                              # sync function that will be executed in AWS Lambda
            import asyncio                                                    # these imports are needed since this code is executed inside ...
            from osbot_utils.utils.Threads import async_invoke_in_new_loop    #    a code environment that doesn't have those imports

            async def an_async_function():                                    # async function to execute from a sync function (which is REALLY hard to do)
                await asyncio.sleep(0.1)                                      # do an await operation to really confirm that we are in async loop
                return "it's 42"                                              # return a string so we can confirm execution

            return  async_invoke_in_new_loop(an_async_function())             # use async_invoke_in_new_loop to run the async function

        assert self.shell.function(execute_in_lambda) == "it's 42"            # get the code of 'execute_in_lambda', send it to AWS Lambda and execute it


    # def test_playwright(self):
    #
    #     def playwright():
    #
    #         import asyncio
    #
    #         async def an_method():
    #             from osbot_utils.utils.Misc import bytes_to_base64
    #             from playwright.async_api import async_playwright
    #             context = await async_playwright().start()
    #             browser = await context.chromium.launch(args=["--disable-gpu", "--single-process"])
    #             page = await browser.new_page()
    #             await page.goto("https://dev.cyber-boardroom.com/web/chat/view/2024-10-03/02/6db0d193-a967-46f0-b623-a2fae56b2434/ba8c382c-57cf-4ef0-bd38-dca0fd30f15e")
    #             await asyncio.sleep(1)
    #
    #             #return page.url
    #             #page_content = await page.content()
    #             # screenshot = await page.screenshot(full_page=True)
    #             # return bytes_to_base64(screenshot)
    #
    #             pdf = await page.pdf(display_header_footer=True, print_background=True)
    #             await context.stop()
    #             return bytes_to_base64(pdf)
    #
    #         def run_in_new_loop():
    #             new_loop = asyncio.new_event_loop()
    #             asyncio.set_event_loop(new_loop)
    #             try:
    #                 return new_loop.run_until_complete(an_method())
    #             finally:
    #                 new_loop.close()
    #
    #
    #         from concurrent.futures import ThreadPoolExecutor
    #         with ThreadPoolExecutor() as pool:
    #             future = pool.submit(run_in_new_loop)
    #             result = future.result()
    #         #result = loop.is_running()
    #         #result = asyncio.run_coroutine_threadsafe(an_method(), loop).result()
    #
    #
    #
    #         return f'{result}'
    #
    #
    #     #pprint(self.shell.function(playwright))
    #
    #
    #     file_data = base64_to_bytes(self.shell.function(playwright))
    #     #pprint(bytes_to_file('./playwright.png', file_data, ))
    #     pprint(bytes_to_file('./playwright.pdf', file_data, ))
    #
    # def test_ls(self):
    #     pprint(self.shell.ls('/tmp'))



    # def install_playwright_browser():
    # from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
    # playwright_cli = Playwright_CLI()
    # result = playwright_cli.install__chrome()
    # return f'{result}'
    # install_result    = self.shell.function(install_playwright_browser)
    # assert install_result           == 'True'

