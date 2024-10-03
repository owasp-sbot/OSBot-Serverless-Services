from osbot_fast_api.api.Fast_API_Routes import Fast_API_Routes
from playwright.async_api               import async_playwright
from playwright.sync_api                import sync_playwright
from starlette.responses                import HTMLResponse


class Routes__Playwright(Fast_API_Routes):
    tag : str = 'playwright'

    def launch_browser(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--disable-gpu", "--single-process"])
            return f'browser launched: {browser}'

    def new_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--disable-gpu", "--single-process"])
            page   = browser.new_page()
            return f'new page: {page}'

    def html(self, url='https://dev.cyber-boardroom.com/config/version'):
        try:
            with sync_playwright() as p:
                #browser = p.chromium.launch(args=["--disable-gpu", "--single-process"])
                browser = p.chromium.launch(args=["--disable-gpu", "--single-process"])
                page    = browser.new_page()
                page.goto(url)
                html_content = page.content()
                return HTMLResponse(content=html_content, status_code=200)
        except Exception as error:
            return f'{error}'

    def html_2(self, url='https://dev.cyber-boardroom.com/config/version'):
        try:
            playwright  = sync_playwright().start()
            browser     = playwright.chromium.launch(args=["--disable-gpu", "--single-process"])
            page        = browser.new_page()
            page.goto(url)
            html_content = page.content()
            #page.screenshot(path="example.png")
            browser.close()
            playwright.stop()
            return html_content

        except Exception as error:
            return f'{error}'

    async def html_async(self, url='https://dev.cyber-boardroom.com/config/version'):
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(args=["--disable-gpu", "--single-process"])
                page    = await browser.new_page()
                await page.goto(url)
                html_content = await page.content()
                return HTMLResponse(content=html_content, status_code=200)
        except Exception as error:
            return f'{error}'


    def setup_routes(self):
        self.add_route_get(self.launch_browser)
        self.add_route_get(self.new_page      )
        self.add_route_get(self.html          )
        self.add_route_get(self.html_2        )
        self.add_route_get(self.html_async    )