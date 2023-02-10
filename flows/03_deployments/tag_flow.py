from parameterized_flow_q4 import etl_parent_flow

# Add a tag to the flow
etl_parent_flow.tags = set(["2019-04-green"])

# Check the tags on the flow
print(etl_parent_flow.tags)
