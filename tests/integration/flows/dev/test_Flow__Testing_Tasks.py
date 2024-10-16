from unittest                                               import TestCase
from osbot_prefect.flows.Flow_Events__To__Prefect_Server    import Flow_Events__To__Prefect_Server
from osbot_serverless_flows.flows.dev.Flow__Testing_Tasks   import Flow__Testing_Tasks


class test_Flow__Testing_Tasks(TestCase):

    def test_run(self):
        with Flow_Events__To__Prefect_Server():
            flow = Flow__Testing_Tasks().run()
            assert flow.flow_return_value == f'flow completed: {flow.flow_id} '
