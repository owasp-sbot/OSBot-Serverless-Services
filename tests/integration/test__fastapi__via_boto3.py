from unittest import TestCase

from osbot_utils.utils.Dev import pprint

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
        assert self.invoke_lambda('/') == { 'body'              : '{"message":"Hello World!"}',
                                            'headers'           : {'content-length': '26', 'content-type': 'application/json'},
                                            'isBase64Encoded'   : False ,
                                            'multiValueHeaders' : {}    ,
                                            'statusCode'        : 200   }

    def test__ping(self):
        assert self.invoke_lambda('/ping') == { 'body'              : '{"pong":"42"}',
                                                'headers'           : {'content-length': '13', 'content-type': 'application/json'},
                                                'isBase64Encoded'   : False ,
                                                'multiValueHeaders' : {}    ,
                                                'statusCode'        : 200   }
