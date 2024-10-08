from unittest import TestCase

from osbot_prefect.flows.Flow_Events__To__Prefect_Server import Flow_Events__To__Prefect_Server
from osbot_utils.utils.Dev import pprint

from osbot_serverless_flows.flows.http.Flow__Http__Raw_Html import Flow__Http__Raw_Html


class test__i__Flow__Http__Raw_Html(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.flow__http_raw_html = Flow__Http__Raw_Html()

    def test_run(self):
        with Flow_Events__To__Prefect_Server():
            with self.flow__http_raw_html.flow__http_raw_html() as _:
                flow = _.execute_flow()
                pprint(flow)