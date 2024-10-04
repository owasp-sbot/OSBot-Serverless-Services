from osbot_serverless_flows.fast_api.Fast_API__Serverless_Flows import Fast_API__Serverless_Flows
from osbot_utils.context_managers.capture_duration import capture_duration

with capture_duration() as duration:
    fast_api__serverless_flows =  Fast_API__Serverless_Flows()
    fast_api__serverless_flows.setup()                           # setup_server
    client__serverless_flows = fast_api__serverless_flows.client()

assert duration.seconds < 1         # make sure the setup time is less than 1 second


def ensure_browser_is_installed():
    from osbot_serverless_flows.playwright.Playwright__Serverless import Playwright__Serverless
    playwright_browser = Playwright__Serverless()
    playwright_browser.browser__install()