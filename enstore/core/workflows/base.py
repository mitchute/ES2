from enum import Enum, auto


class ExecutionType(Enum):
    SERIAL = auto()
    PARALLEL = auto()


class BaseWorkflow(object):
    def __init__(self, execution_type=None):
        self.execution_type = self.set_execution_type(execution_type)

    @staticmethod
    def set_execution_type(execution_type: str):
        execution_type = execution_type.lower()
        if execution_type == "parallel":
            return ExecutionType.PARALLEL
        elif execution_type == "serial":
            return ExecutionType.SERIAL
        else:
            raise ValueError(f"Workflow execution type '{execution_type}' is not valid.")
