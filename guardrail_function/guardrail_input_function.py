from typing import Any
from agents import Agent, RunContextWrapper,GuardrailFunctionOutput,Runner, input_guardrail, output_guardrail
from my_agent.guardrail_agents import guardrail_agent
from my_config.conf import MODEL

@input_guardrail
async def guardrail_input_function(ctx: RunContextWrapper, agent , input):
    result = await Runner.run(guardrail_agent, input=input , context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_query_about_known_hotel
    )



