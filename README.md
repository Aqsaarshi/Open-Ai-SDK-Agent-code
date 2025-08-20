# 🧠 OpenAI Agent SDK Assignments  

This repository contains multiple assignments showcasing the use of **OpenAI Agent SDK** with features like **guardrails, dynamic instructions, custom tools, and customer support bots**.  

---

## 📌 Assignment 1: Guardrail Hotel Assistant  

### 🎯 Objective  
Build an AI Hotel Customer Care Assistant that:  
- Uses **input guardrails** to validate queries (only hotel-related).  
- Uses **output guardrails** to block political topics.  
- Dynamically injects hotel data into the assistant’s instructions.  
- Provides hotel information if a hotel name is detected in the query, otherwise asks the user for it.  

### 🛠 Key Features  
- Dynamic instructions generated from a `hotels` dictionary.  
- Guards against irrelevant queries.  
- Example hotels: **Sannata**, **Sunshine**, **BeachView**.  

---

## 📌 Assignment 2: Custom Web Search Tool  

### 🎯 Objective  
Build a **custom web search tool** using the **Tavily API** to fetch results and integrate it with an AI Agent.  

### 🛠 Key Features  
- Explores and uses **Tavily API**.  
- Fetches search results programmatically.  
- Can be integrated with an AI Agent for **question answering**.  

---

## 📌 Assignment 3: Convert Static Instructions into Dynamic Instructions  

### 🎯 Objective  
Convert **static agent instructions** into **dynamic instructions** using **OpenAI’s Agent SDK**.  

The assistant should:  
- Handle **multiple hotels** by storing and retrieving details dynamically.  
- Use **context** to return the correct hotel information based on the user’s query.  

### 🛠 Features  
- Built using **OpenAI’s Agent SDK**.  
- Supports multiple hotels with **context-driven responses**.  
- More flexible compared to static hardcoded instructions.  

---

## 📌 Assignment 4: Smart Customer Support Bot (SDK)  

### 🎯 Objective  
Simulate a **Smart Customer Support Assistant** built with OpenAI Agent SDK.  
It demonstrates **guardrails, tool usage, FAQs, order tracking, and human agent handoff**.  

### 🛠 Features  
- **Guardrails** → Blocks negative or offensive queries (`block_negative_input`).  
- **Order Status Lookup** → Uses a simulated database (`1001`, `1002`, `1003`) to return statuses like *Shipped*, *Processing*, *Delivered*.  
- **FAQs** → Answers simple questions (e.g., hotel room details).  
- **Agent Handoff** → Escalates unsupported or complex queries to a **Human Agent**.  
- **Interactive Chat Loop** → Users can chat with the bot in real-time.  

---

