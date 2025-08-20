from agents import Agent
from my_config.conf import MODEL
from tool_basic import get_plus

assistant = Agent(
    name = "My Math teacher",
    instructions="You are a helpful math teacher.",
    model=MODEL,
    )
