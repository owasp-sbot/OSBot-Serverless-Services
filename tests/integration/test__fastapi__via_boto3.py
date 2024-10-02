from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import list_set

from osbot_aws.aws.lambda_.Lambda import Lambda
from osbot_aws.aws.session.Session__Kwargs__Lambda import Session__Kwargs__Lambda
from osbot_aws.testing.Temp__Random__AWS_Credentials import Temp__Random__AWS_Credentials



class test__fastapi__via_boto3(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.function_name          = 'function'
        cls.endpoint_url           = 'http://localhost:5002/'
        cls.session_kwargs__lambda = Session__Kwargs__Lambda(endpoint_url=cls.endpoint_url).__locals__()

    def invoke_lambda(self, path):
        with Temp__Random__AWS_Credentials():
            with Lambda(name=self.function_name, session_kwargs__lambda=self.session_kwargs__lambda) as _:
                payload = { "resource"      : ""    ,
                            "requestContext": {}    ,
                            "httpMethod"    : "GET" ,
                            "path"          : path  }
                response = _.invoke(payload)
                return response

    def test__root(self):
        response = self.invoke_lambda('/')
        assert response.get('body'      )        == ""
        assert response.get('statusCode')        == 307
        assert list_set(response.get('headers')) == ['content-length', 'fast-api-request-id', 'location']

    def test__ping(self):
        response = self.invoke_lambda('/info/ping')
        assert response.get('body'      )         == '{"pong":"42"}'
        assert response.get('statusCode')        == 200
        assert list_set(response.get('headers')) == ['content-length', 'content-type', 'fast-api-request-id']

