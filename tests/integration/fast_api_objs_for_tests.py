from osbot_serverless_flows.fast_api.Fast_API__Serverless_Flows             import Fast_API__Serverless_Flows
from osbot_serverless_flows.utils.OSBot_Serverless_Flows__Local_Stack       import OSBot_Serverless_Flows__Local_Stack
from osbot_utils.context_managers.capture_duration import capture_duration

DEFAULT_TEST__AWS_ACCOUNT_ID = '0000111100001111'

with OSBot_Serverless_Flows__Local_Stack() as _:
    osbot_serverless__flows_local_stack               = _
    _.temp_asw_credentials.env_vars['AWS_ACCOUNT_ID'] = DEFAULT_TEST__AWS_ACCOUNT_ID
    _.activate()                                            # todo : see side effects of putting this here


with capture_duration() as duration:
    fast_api__serverless_flows =  Fast_API__Serverless_Flows()
    fast_api__serverless_flows.setup()                           # setup_server
    client__serverless_flows = fast_api__serverless_flows.client()

assert duration.seconds < 1         # make sure the setup time is less than 1 second


def ensure_browser_is_installed():
    from osbot_serverless_flows.playwright.Playwright__Serverless import Playwright__Serverless
    playwright_browser = Playwright__Serverless()
    playwright_browser.browser__install()