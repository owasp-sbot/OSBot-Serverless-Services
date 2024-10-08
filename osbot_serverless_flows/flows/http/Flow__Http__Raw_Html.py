from osbot_utils.helpers.flows.decorators.task import task

from osbot_utils.helpers.flows.Flow import Flow

from osbot_utils.helpers.flows.decorators.flow import flow

from osbot_utils.base_classes.Type_Safe import Type_Safe


class Flow__Http__Raw_Html(Type_Safe):

    @task()
    def check_config(self):
        print('checking config')

    @flow()
    async def flow__http_raw_html(self) -> Flow:
        self.check_config()

    def run(self):
        with self.flow__http_raw_html() as _:
            _.execute_flow()
            return _
            #return _.data