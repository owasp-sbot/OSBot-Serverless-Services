from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from osbot_serverless_flows.s3_minio.Flow__Event__From_S3_Minio import Flow__Event__From_S3_Minio


class test_Flow__Event__From_S3_Minio(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.flow_event_from_s3_minio = Flow__Event__From_S3_Minio()

    # def test_s3_bucket(self):
    #     with self.flow_event_from_s3_minio as _:
    #         pprint(_.s3_bucket())