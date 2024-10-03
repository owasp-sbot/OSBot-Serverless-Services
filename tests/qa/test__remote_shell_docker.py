# from unittest import TestCase
#
# from osbot_serverless_flows.utils._for_osbot_aws.Http__Remote_Shell import Http__Remote_Shell
#
#
# class test__remote_shell_docker(TestCase):
#
#     def setUp(self):
#         self.port  = 5002
#         target_url = f'http://localhost:{self.port}/debug/an-method'
#         self.shell = Http__Remote_Shell(target_url=target_url)
#
#     def test_lambda_shell_setup(self):
#         assert self.shell.ping() == 'pong'
#
#     def test_ping(self):
#         def ping():
#             return 'here....'
#         self.shell.function__print(ping)
#
#
#     def test_playwright(self):
#         def playwright():
#             from playwright.sync_api import sync_playwright
#
#             with sync_playwright() as p:
#                 browser = p.chromium.launch()
#                 page = browser.new_page()
#                 page.goto("http://playwright.dev")
#                 title = page.title()
#                 browser.close()
#             return title
#         self.shell.function__print(playwright)