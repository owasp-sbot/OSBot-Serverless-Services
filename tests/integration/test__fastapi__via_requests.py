import requests
from unittest import TestCase
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

    def test__root(self):
        payload = create_payload_for_path('/')
        response = requests.post(self.invoke_url, headers=self.headers , json=payload)
        assert response.status_code == 200
        assert response.json() == { 'body'              : '{"message":"Hello World!"}',
                                    'headers'           : {'content-length': '26', 'content-type': 'application/json'},
                                    'isBase64Encoded'   : False ,
                                    'multiValueHeaders' : {}    ,
                                    'statusCode'        : 200   }

    def test__ping(self):
        payload  = create_payload_for_path('/ping')
        response = requests.post(self.invoke_url, headers=self.headers, json=payload)
        assert response.status_code == 200
        assert response.json() == { 'body'              : '{"pong":"42"}',
                                    'headers'           : {'content-length': '13', 'content-type': 'application/json'},
                                    'isBase64Encoded'   : False ,
                                    'multiValueHeaders' : {}    ,
                                    'statusCode'        : 200   }

    def test__docs(self):
        payload  = create_payload_for_path('/docs')
        response = requests.post(self.invoke_url, headers=self.headers, json=payload)
        assert response.status_code == 200
        assert "Swagger UI" in response.text

    # def test__openapi(self):
    #     payload  = create_payload_for_path('/openapi.json')
    #     response = requests.post(self.invoke_url, headers=self.headers, json=payload)
    #     assert response.status_code == 200
    #     open_api_json = json_parse(response.json().get('body'))
    #     assert open_api_json == { 'info': {'title': 'FastAPI', 'version': '0.1.0'},
    #                               'openapi': '3.1.0',
    #                               'paths': { '/': { 'get': { 'operationId': 'root__get',
    #                                                          'responses': { '200': { 'content': { 'application/json': { 'schema': { }}},
    #                                                                                  'description': 'Successful '
    #                                                                                                 'Response'}},
    #                                                          'summary': 'Root'}},
    #                                          '/ping': { 'get': { 'operationId': 'ping_ping_get',
    #                                                              'responses': { '200': { 'content': { 'application/json': { 'schema': { }}},
    #                                                                                      'description': 'Successful '
    #                                                                                                     'Response'}},
    #                                                              'summary': 'Ping'}},
    #                                          '/version': {'get': {'operationId': 'version_version_get',
    #                                                               'responses': {'200': {
    #                                                                   'content': {'application/json': {'schema': {}}},
    #                                                                   'description': 'Successful '
    #                                                                                  'Response'}},
    #                                                               'summary': 'Version'}}
    #                                          }}


    def test__version(self):
        payload  = create_payload_for_path('/version')
        response = requests.post(self.invoke_url, headers=self.headers, json=payload)
        assert response.status_code == 200
        assert response.json().get('body') == f'"{version__osbot_serverless_flows}"'