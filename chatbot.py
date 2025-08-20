from agents import Runner
import chainlit as cl
from my_agent.teacher import math_teacher  # ✅ Only import what's needed

@cl.on_message
async def main(message: cl.Message):
    prompt = message.content

    # Run the email assistant synchronously
    result = Runner.run_sync(math_teacher, prompt)

    # Send response
    await cl.Message(content=f"Received: {result.final_output }").send()
