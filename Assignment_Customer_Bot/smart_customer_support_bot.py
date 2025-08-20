# ASSIGNMENT: Smart Customer Support Bot (SDK)
# -------------------------------------------------
# This program simulates a smart customer support assistant that:
# 1. Uses an input guardrail to block negative queries.
# 2. Provides order status information from a simulated database (API).
# 3. Answers FAQ-style queries (e.g., hotel room details).
# 4. Hands off complex or negative queries to a human agent.
# 5. Runs an interactive chatbot loop where users can type queries.


import asyncio
import logging
from agents import Agent, RunContextWrapper, GuardrailFunctionOutput
from block_negative_function import block_negative_input

# --- Logging setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# --- Step 1: Orders database (simulated API) ---
orders = {
    "1001": "Shipped",
    "1002": "Processing",
    "1003": "Delivered"
}

# --- Step 2: Async function for order status ---
async def get_order_status(order_id):
    logging.info(f"Tool called for order_id: {order_id}")
    return orders.get(order_id, f"Order ID {order_id} not found!")

# --- Step 3: Human Agent ---
HumanAgent = Agent(
    name="HumanAgent",
    instructions="Handle complex or negative queries."
)

async def human_handoff(query):
    logging.info(f"Handoff to human agent for query: {query}")
    return f"📞 Handoff to human agent: {query}"

# --- Step 4: Bot Agent ---
BotAgent = Agent(
    name="BotAgent",
    instructions="Answer FAQs and fetch order status using function tools.",
    model_settings={"tool_choice": "auto", "metadata": {"store_id": "123"}}
)

# --- Step 5: Bot response logic ---
async def bot_response(query):
    # 1️⃣ Guardrail check using async block_negative_input
    ctx = RunContextWrapper(context={})
    guard_output_obj: GuardrailFunctionOutput = await block_negative_input(ctx, BotAgent, query)
    if guard_output_obj.tripwire_triggered:
        return guard_output_obj.output_info

    # 2️⃣ FAQ example
    if "rooms" in query.lower():
        return "🏨 Hotel Sannata has a total of 200 rooms."

    # 3️⃣ Order status
    if "order" in query.lower():
        order_id = query.split()[-1]
        return await get_order_status(order_id)

    # 4️⃣ Unknown / complex query → human handoff
    return await human_handoff(query)

# --- Step 6: Run the bot ---
async def main():
    print("Welcome to Smart Customer Support Bot! Type 'exit' to quit.\n")
    while True:
        user_input = input("👉 Ask your query: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = await bot_response(user_input)
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
