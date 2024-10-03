import requests
from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Json import json_parse

from osbot_serverless_flows.utils.Version import version__osbot_serverless_flows


def create_payload_for_path(path):
    return  {   "resource"      : ""    ,
                "requestContext": {}    ,
                "httpMethod"    : "GET" ,
                "path"          : path  }

class test__fastapi__via_requests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.function_name = 'function'
        cls.function_server = 'http://localhost:5002'
        cls.headers = {'Content-Type': 'application/json'}
        cls.invoke_url = f"{cls.function_server}/2015-03-31/functions/{cls.function_name}/invocations"

    def test__ping(self):
        payload             = create_payload_for_path('/info/ping')
        response            = requests.post(self.invoke_url, headers=self.headers, json=payload)
        fast_api_request_id = response.json().get('headers').get('fast-api-request-id')

        assert response.status_code == 200
        assert response.json()      == { 'body'              : '{"pong":"42"}',
                                         'headers'           : {'content-length'     : '13'                ,
                                                                'content-type'       : 'application/json'  ,
                                                                'fast-api-request-id': fast_api_request_id },
                                         'isBase64Encoded'   : False ,
                                         'multiValueHeaders' : {}    ,
                                         'statusCode'        : 200   }

    def test__docs(self):
        payload  = create_payload_for_path('/docs')
        response = requests.post(self.invoke_url, headers=self.headers, json=payload)
        assert response.status_code == 200
        assert "Swagger UI" in response.text



    def test__version(self):
        payload  = create_payload_for_path('/info/version')
        response = requests.post(self.invoke_url, headers=self.headers, json=payload)
        assert response.status_code == 200
        assert response.json().get('body') == f'{{"version":"{version__osbot_serverless_flows}"}}'
