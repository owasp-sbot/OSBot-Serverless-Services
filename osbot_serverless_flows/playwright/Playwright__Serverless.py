from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
from osbot_utils.utils.Dev import pprint

from osbot_utils.utils.Threads import async_invoke_in_new_loop
from playwright.async_api import async_playwright, Playwright

from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from osbot_utils.base_classes.Type_Safe             import Type_Safe

class Playwright__Serverless(Type_Safe):
    playwright     : Playwright          = None
    playwright_cli : Playwright_CLI



    @cache_on_self
    def chrome_path(self):
        return self.playwright_cli.executable_path__chrome()

    async def browser(self):
        playwright = await self.start()
        return await playwright.chromium.launch(**self.browser__launch_kwargs())

    async def new_page(self):
        browser = await self.browser()
        return await browser.new_page()

    async def goto(self, url):
        page = await self.new_page()
        return await page.goto(url)

    async def start(self) -> Playwright:
        self.playwright = await async_playwright().start()
        return self.playwright



    # context = await async_playwright().start()

    #             browser = await context.chromium.launch(**launch_kwargs)
    #             page    = await browser.new_page()
    #             await page.goto                 (url)
    #
    #             screenshot = await page.screenshot(full_page=True)
    #             return bytes_to_base64(screenshot)


    # sync methods

    def browser__exists(self):
        return self.playwright_cli.browser_installed__chrome()

    def browser__install(self):                                     # todo: see if we use the version that was downloaded during the docker image install
        if self.browser__exists() is False:                         #       which is downloaded to: /root/.cache/ms-playwright/chromium-1134
            return self.playwright_cli.install__chrome()            #       and                   : /root/.cache/ms-playwright/ffmpeg-1010
        return True

    def browser__launch_kwargs(self):
        return dict(args=["--disable-gpu", "--single-process"],
                    executable_path=self.chrome_path())