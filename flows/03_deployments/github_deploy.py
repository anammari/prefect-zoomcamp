import prefect
from prefect import Flow, Task
from prefect.storage import GitHub

# Create a Task to represent your Prefect flow
class MyFlowTask(Task):
    def run(self):
        # Import the flow from your "parameterized_flow_q4.py" script
        from parameterized_flow_q4 import etl_parent_flow
        # Run the flow
        etl_parent_flow.run()


# Initialize a Flow object
flow = Flow("My Prefect Flow", storage=GitHub(repo="https://github.com/anammari/prefect-zoomcamp"))

# Add the MyFlowTask to the flow
task = MyFlowTask()
flow.add_task(task)

# Register the flow with Prefect Cloud
flow.run()
