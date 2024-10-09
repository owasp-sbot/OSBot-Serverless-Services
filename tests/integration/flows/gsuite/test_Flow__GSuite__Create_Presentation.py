from unittest                                                               import TestCase
from osbot_prefect.flows.Flow_Events__To__Prefect_Server                    import Flow_Events__To__Prefect_Server
from osbot_serverless_flows.flows.gsuite.Flow__GSuite__Create_Presentation  import Flow__GSuite__Create_Presentation
from osbot_utils.utils.Env                                                  import load_dotenv


class test_Flow__GSuite__Create_Presentation(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()
        cls.flow__create_presentation = Flow__GSuite__Create_Presentation()

    def test_run(self):
        with Flow_Events__To__Prefect_Server():
            with self.flow__create_presentation.flow__create_presentation() as _:
                flow = _.execute_flow()