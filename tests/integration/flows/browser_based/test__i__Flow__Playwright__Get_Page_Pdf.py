from unittest                                                                         import TestCase

from osbot_utils.utils.Dev import pprint

from osbot_serverless_flows.flows.browser_based.Flow__Playwright__Get_Page_Pdf import Flow__Playwright__Get_Page_Pdf
from tests.integration.fast_api_objs_for_tests import ensure_browser_is_installed
from osbot_utils.utils.Misc import base64_to_bytes

from osbot_serverless_flows.flows.browser_based.Flow__Playwright__Get_Page_Screenshot import Flow__Playwright__Get_Page_Screenshot


class test__i__Flow__Playwright__Get_Page_Pdf(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        ensure_browser_is_installed()
        cls.flow__get_page_pdf = Flow__Playwright__Get_Page_Pdf()

    def test_run(self):
        flow_data  = self.flow__get_page_pdf.run()
        pdf_bytes  = flow_data.get('pdf_bytes' )
        pdf_base64 = flow_data.get('pdf_base64')

        assert pdf_bytes.startswith(b'%PDF-1.4') is True
        assert len(pdf_bytes )                 > 10000
        assert len(pdf_base64)                 > 10000
        assert base64_to_bytes(pdf_base64)     == pdf_bytes
