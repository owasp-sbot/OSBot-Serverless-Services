import requests
from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Json import json_parse

from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows


# def create_payload_for_path(path):
#     return  {   "resource"      : ""    ,
#                 "requestContext": {}    ,
#                 "httpMethod"    : "GET" ,
#                 "path"          : path  }

class test__fastapi__via_requests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.function_name = 'function'
        cls.function_server = 'http://localhost:5002'
        cls.headers = {'Content-Type': 'application/json'}
        #cls.invoke_url = f"{cls.function_server}/2015-03-31/functions/{cls.function_name}/invocations"

    def test__ping(self):
        url                           = f"{self.function_server}/info/ping"
        response                      = requests.get(url)
        response__fast_api_request_id = response.headers.get('fast-api-request-id')
        response__date                = response.headers.get('date')
        assert response.status_code == 200
        assert response.json()      == {"pong":"42"}
        assert response.headers     == {'content-length'     : '13'                          ,
                                        'content-type'       : 'application/json'            ,
                                        'date'               : response__date                ,
                                        'fast-api-request-id': response__fast_api_request_id ,
                                        'server'             : 'uvicorn'                     }

    def test__docs(self):
        url      = f"{self.function_server}/docs"
        response = requests.get(url)
        assert response.status_code == 200
        assert "Swagger UI" in response.text



    def test__version(self):
        url = f"{self.function_server}/info/version"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json() == {"version": version__osbot_serverless_flows}
