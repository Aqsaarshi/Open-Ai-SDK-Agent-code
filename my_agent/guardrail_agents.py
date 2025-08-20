from agents import Agent
from my_config.conf import MODEL
from my_schema.my_data_type import MyDataType, OutputCheck


guardrail_agent = Agent(
    name="Guardrail Agent For Hotel",
    instructions="Check queries for hotel Sannata",
    model=MODEL,
    output_type=MyDataType
)


output_guardrail_agent = Agent(
    name="OutputGuardrailAgent",
    instructions="""
    Check if the given text contains political content or references to political figures.
    Return true if yes, otherwise false.
    """,
    model=MODEL,
    output_type=OutputCheck
)