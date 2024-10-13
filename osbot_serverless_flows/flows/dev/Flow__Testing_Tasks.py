from osbot_utils.helpers.flows import Flow
from osbot_utils.helpers.flows.decorators.flow import flow

from osbot_utils.helpers.flows.decorators.task import task

from osbot_utils.base_classes.Type_Safe import Type_Safe


class Flow__Testing_Tasks(Type_Safe):

    @task()
    def task_1(self):
        print('inside task_1')
        return "task 1 data"

    @task()
    def task_2(self):
        print('inside task_2')
        self.task_3()
        return "task 2 data"

    @task()
    def task_3(self):
        print('inside task_3')
        return "task 3 data"

    @flow()
    def flow__testing_tasks(self) -> Flow:
        self.task_1()
        self.task_2()
        return "flow completed"

    def run(self) -> Flow:
        with self.flow__testing_tasks() as _:
            return _.execute_flow()