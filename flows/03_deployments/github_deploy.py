from prefect.deployments import Deployment
from parameterized_flow_q4 import etl_parent_flow
from prefect.filesystems import GitHub

github_block = GitHub.load("github-zoom")

github_dep = Deployment.build_from_flow(
    flow=etl_parent_flow,
    name="github-flow",
    storage=github_block,
    entrypoint="flows\03_deployments\parameterized_flow_q4.py"
)


if __name__ == "__main__":
    github_dep.apply()
