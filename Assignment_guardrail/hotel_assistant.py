#Assignment: Guardrail Hotel Assistant
# This program is an AI Hotel Customer Care Assistant that:

# Checks every query using an input guardrail function (to verify if it’s a valid hotel query or not).

# Applies an output guardrail (to block political topics).

# Dynamically injects hotel data into the assistant’s instructions.

# If the user specifies a hotel name in the query, it provides information about that hotel.
# Otherwise, it asks the user for the hotel name.



import asyncio
from agents import (
    Agent,
    Runner,
    set_tracing_disabled,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered
)
from guardrail_function.guardrail_input_function import guardrail_input_function
from guardrail_function.guardrail_output_function import block_political_output
from my_config.conf import MODEL

set_tracing_disabled(True)

hotels = {
    "Sannata": {"rooms": 200,"owner":"Mr Ratan Lal","reserved":20},
    "Sunshine": {"rooms": 150,"owner":"Mrs. Aqsa","reserved":30},
    "BeachView": {"rooms": 200,"owner":"Mr Bilal","reserved":20},
}

def dynamic_instructions(run_context, agent):
    hotel_name = None
    if hasattr(run_context, "context") and run_context.context:
        hotel_name = run_context.context.get("hotel")

    if hotel_name in hotels:
        info = hotels[hotel_name]
        return f"""
        You are a helpful customer care assistant.
        Hotel name: {hotel_name}.
        Total rooms: {info['rooms']}.
        Owner: {info['owner']}.
        Reserved rooms: {info['reserved']}.
        """
    return "You are a hotel assistant. Ask the user which hotel they are interested in."

hotel_assistant = Agent(
    name="Hotel Assistant",
    instructions=dynamic_instructions,
    model=MODEL,
    input_guardrails=[guardrail_input_function],
    output_guardrails=[block_political_output]
)


# Test input guardrail
user_input = input("👉 Ask your queries about Hotel: ")

# Dynamic hotel detection
context_hotel = None
for name in hotels.keys():
    if name.lower() in user_input.lower():
        context_hotel = name
        break

try:
    res = Runner.run_sync(
        starting_agent=hotel_assistant,  # ✅ Agent object yahan
        input=user_input,
        context={"hotel": context_hotel} if context_hotel else {}
    )
    print(res.final_output)
except InputGuardrailTripwireTriggered:
    print("❌ This query is not about any known Hotel")
except OutputGuardrailTripwireTriggered:
    print("⚠ Political or blocked topic detected.")
