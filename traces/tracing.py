from agents import RunConfig, Runner, set_tracing_export_api_key,trace
from decouple import config
from my_agent.assistant import assistant 

openai_api_key = config("OPENAI_API_KEY")

set_tracing_export_api_key(openai_api_key)


with trace("My Test WorkFlow"):
    res = Runner.run_sync(
        starting_agent= assistant ,#assistant 
        input="5+2= ?",
    )

    result = Runner.run_sync(
        starting_agent= assistant ,#assistant 
        input=f"{res.final_output}*1000",
        run_config=RunConfig(tracing_disabled=False) #true means tracing krni ha mtlb code chly ga but tracing nhi hogi 

        
    )

    print(result.final_output)
