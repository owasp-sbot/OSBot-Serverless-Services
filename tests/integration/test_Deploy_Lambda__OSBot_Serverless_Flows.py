from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from deploy.docker.lambdas.Deploy_Lambda__OSBot_Serverless_Flows import Deploy_Lambda__OSBot_Serverless_Flows


class test_Deploy_Lambda__OSBot_Serverless_Flows(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deploy_lambda = Deploy_Lambda__OSBot_Serverless_Flows()

    def test_ecr_image_uri(self):
        with self.deploy_lambda as _:
            ecr_image_uri = _.ecr_image_uri()
            pprint(ecr_image_uri)
