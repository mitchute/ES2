from enstore.core.workflows.base import BaseWorkflow, ExecutionType


class WorkflowMgr(object):
    def __init__(self, workflows: list):
        self.workflows = workflows  # type: list[BaseWorkflow]

    def execute_workflows(self):
        for idx, wf in enumerate(self.workflows):
            if wf.execution_type is ExecutionType.SERIAL:
                self.execute_serial_workflows(idx)
            elif wf.execution_type is ExecutionType.PARALLEL:
                self.execute_parallel_workflows(idx)

    def execute_serial_workflows(self, wf_num: int):
        pass

    def execute_parallel_workflows(self, wf_num: int):
        pass
