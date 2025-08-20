import asyncio
from agents import Runner
from my_agent.language import triage_agent 
from my_agent.teacher import math_teacher, agent

res = Runner.run_sync(
        starting_agent=triage_agent,
        input="karachi ka moosam kaisa ha and 12-2",
        context={"name": "Aqsa Arshad" , "age" : 30, "role": "teacher"} #age ky hisaab sy tool chly ga validate_tool ki file sy 
        #max_turns=2
    )
print(res.final_output)












# #"This is for Chainlit code"
# # main.py
# #  import chainlit as cl
# # from agents import Runner
# # from my_agent.teacher import email_writer  # ✅ your agent
# # from my_config.conf import MODEL  # (if needed)

# # @cl.on_message
# # async def main(message: cl.Message):
# #     user_input = message.content

# #     # Run your agent using Runner
# #     result = await Runner.run(email_writer, user_input)

# #     # Send the output back to Chainlit UI
# #     await cl.Message(content=result.final_output).send()









