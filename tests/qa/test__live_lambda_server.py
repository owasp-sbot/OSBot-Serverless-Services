from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Http import GET


class test__live_lambda_server(TestCase):

    def test__invoke_url(self):
        live_url = 'https://a4sbatx723cfs7tw3kbiifv37q0evpcp.lambda-url.eu-west-1.on.aws'

        pprint(GET(live_url))