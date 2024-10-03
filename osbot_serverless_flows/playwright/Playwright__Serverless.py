from osbot_playwright.playwright.api.Playwright_CLI import Playwright_CLI
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from osbot_utils.base_classes.Type_Safe             import Type_Safe

class Playwright__Serverless(Type_Safe):
    playwright_cli : Playwright_CLI

    @cache_on_self
    def chrome_path(self):
        return self.playwright_cli.executable_path__chrome()
