from osbot_fast_api.api.Fast_API_Routes import Fast_API_Routes

from osbot_serverless_flows.flows.dev.Flow__Testing_Tasks import Flow__Testing_Tasks


class Routes__Dev(Fast_API_Routes):
    tag : str = 'dev'

    def flow_testing_tasks(self):
        with Flow__Testing_Tasks() as _:
            return _.run().flow_return_value

    def setup_routes(self):
        self.add_route_get(self.flow_testing_tasks)