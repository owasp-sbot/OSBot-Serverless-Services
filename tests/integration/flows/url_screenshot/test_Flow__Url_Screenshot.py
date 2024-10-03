# from unittest import TestCase
#
# from osbot_playwright.playwright.api.Playwright_Browser__Chrome import Playwright_Browser__Chrome
# from osbot_utils.utils.Dev import pprint
#
#
# class test_Flow__Url_Screenshot(TestCase):
#
#     def test_playwright(self):
#         headless = False
#         browser = Playwright_Browser__Chrome(headless=headless)
#         browser.install()
#         pprint(browser.is_installed() )
#         pprint(browser.browser_exec_path)
#         pprint(browser.playwright_cli.dry_run())
#         #new_page = browser.new_page()
#         #pprint(new_page)
#         # from osbot_serverless_flows.flows.url_screenshot.Flow__Url_Screenshot import Flow__Url_Screenshot
#
#     def test_open_playwright(self):
#
#         browser_chrome = Playwright_Browser__Chrome()
#         browser = browser_chrome.browser()
#         pprint(browser)
#         page = browser.new_page()
#         pprint(page)
#         pprint(page.goto('https://www.google.com'))
#         pprint(page.url)
#
#         browser_chrome.stop_playwright_and_process()
