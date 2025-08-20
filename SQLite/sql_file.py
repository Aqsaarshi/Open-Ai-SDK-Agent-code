from agents import Runner, set_tracing_disabled, SQLiteSession # " yaha pr old data save kr sakhty ha "
from my_agent.language import triage_agent

# Tracing disable
set_tracing_disabled(True)

# SQLite session create
session = SQLiteSession("user1","conversation.db")

while True:
    prompt = input("write prompt here!!: ")
    if prompt.lower() == "exit":
        break
    
    res = Runner.run_sync(
        starting_agent=triage_agent,
        input=prompt,
        session=session
    )
    
    print(res.final_output)
