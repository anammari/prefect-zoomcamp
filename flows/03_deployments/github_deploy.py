from prefect import Flow, Task
from prefect.engine.executors import LocalDaskExecutor
from prefect.storage import GitHub

# Import your Prefect flow
from parameterized_flow_q4 import etl_parent_flow

# Create a Task to represent your Prefect flow
class MyFlowTask(Task):
    def run(self, flow_reference: str = "flows/03_deployments/parameterized_flow_q4.etl_parent_flow"):
        # Load the flow from your forked GitHub repository
        with open(flow_reference, "r") as file:
            exec(file.read(), globals())
        
        # Return the flow object
        return eval(flow_reference)

# Create the Prefect flow
with Flow("My Prefect Flow", storage=GitHub(repo="anammari/prefect-zoomcamp")) as flow:
    task = MyFlowTask()

# Deploy the Prefect flow
flow.run(executor=LocalDaskExecutor())
