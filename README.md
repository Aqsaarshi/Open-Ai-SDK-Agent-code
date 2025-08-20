📌 Assignment 1: Guardrail Hotel Assistant

Objective:
Build an AI Hotel Customer Care Assistant that:

Uses input guardrails to validate queries (only hotel-related).

Uses output guardrails to block political topics.

Dynamically injects hotel data into the assistant’s instructions.

Provides hotel information if a hotel name is detected in the query, otherwise asks the user for it.

Key Features:

Dynamic instructions generated from a hotels dictionary.

Guards against irrelevant queries.

Example hotels: Sannata, Sunshine, BeachView.

📌 Assignment 2 : Custom Web Search Tool

Objective:
Build a custom web search tool using the Tavily API to fetch results and integrate it with an AI Agent.

🎯 Key Features:

Explores and uses Tavily API.

Fetches search results programmatically.

Can be integrated with an AI agent for question answering.


## 📌 Assignment 3: Convert Static Instructions into Dynamic Instructions

### 🎯 Objective
The goal of this assignment is to **convert static agent instructions into dynamic ones** using OpenAI’s Agent SDK.  

The assistant should be capable of handling **multiple hotels** by storing and retrieving hotel details dynamically, instead of relying on hardcoded/static values.

---

## 🛠 Features
- Uses **OpenAI’s Agent SDK**.  
- Can **store and retrieve hotel details** for multiple hotels.  
- Dynamically uses **context** to return correct hotel information based on the user’s query. 



🛠️ Assignment: 4 Smart Customer Support Bot (SDK)

This program simulates a Smart Customer Support Assistant built with OpenAI Agent SDK.
It demonstrates guardrails, tool usage, FAQs, order tracking, and human agent handoff.

🎯 Features

Guardrails

Blocks negative or offensive queries using block_negative_input.

Order Status Lookup

Simulated order database (e.g., Order IDs 1001, 1002, 1003).

Retrieves order status like Shipped, Processing, Delivered.

FAQs

Answers simple FAQs (e.g., number of hotel rooms).

Agent Handoff

Complex or unsupported queries are escalated to a Human Agent.

Interactive Chat Loop

Users can chat in real time with the bot. 




Type exit or quit to stop the program.

