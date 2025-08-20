from agents import Agent, ModelSettings
from agents.agent import StopAtTools
from my_config.conf import MODEL
from my_schema.agent_output import MyDataOutput
from tool_basic import get_multiply , get_plus , get_subtract , subtract



math_teacher = Agent(
    name = "Math teacher",
    instructions="You are a helpful math teacher.",
    model=MODEL,
    tools=[get_multiply , get_plus , get_subtract , subtract],
    #tool_use_behavior="run_llm_again",
    #tool_use_behavior=StopAtTools(stop_at_tools_names=["get_plus","get_multiply"]),  # YA JAB USE KARAIN GY JAB LLM KO ROOKNA HOGA 
    #model_settings=ModelSettings(tool_choice="get_subtract" , parallel_tool_calls=False), # YAHA HUM auto , none , required use bhi KRTY HA 
    #reset_tool_choice=True,
    #output_type=MyDataOutput,
    #output_type=MyData    # YA BHI HUM USE KRSAKHTY HA FULL DATA K LIY 
    

)
#YA IK TOOL CALLING HA ik AGENT MAIN TOOL PASS KRDIA HA TO AGENT--> TOOL KO DYGA-->PHIR WAPIS TOOL --> AGENT KO ANSWER DY GA    
agent = Agent(
    name = "Aqsa Arshad",
    instructions="You are helpfull assistant",
    model=MODEL,
    tools=[
        math_teacher.as_tool(tool_name="math_teacher",
        tool_description="This is math tool")
    ],
)

#print(agent)








# email_writer = Agent(
#     name="Email Assistant",
#     instructions=(
#         "First greet the user, then create a complete email.\n"
#         "You are an AI Email Assistant. Users will describe the kind of email they want to write in any language "
#         "(English, Roman Urdu, or Urdu).\n"
#         "Based on their input, write a clear, polite, and professional email in English with a subject and body.\n"
#         "Do NOT ask follow-up questions. Use your best guess for missing details.\n"
#         "Keep the tone general and helpful if not specified."
#     ),
#     model="gemini-2.0-flash",


#     tools=[get_weather]
# )
