from agents import Agent, enable_verbose_stdout_logging , handoff
from my_config.conf import MODEL
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from service.service_function import service
from my_schema.input_schema import MyInputData
from tool_basic import get_weather
from agents.extensions import handoff_filters
from validator.validate_tool import tool_validate




# Create Next.js assistant agent
next_js_assistant = Agent(
    name="Next.js Agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    You are a helpful Next.js assistant.""",
    model=MODEL,
    handoff_description="This is helpul Next.js assistant"
)    

# Create Python assistant agent
python_assistant = Agent(
    name="Python Agent",
    instructions="You are a helpful Python assistant.",
    model=MODEL
)


math_assistant = Agent(
    name="Math Agent",
    instructions="You are a helpful Math assistant.",
    model=MODEL,
)


math_teacher = handoff(
    agent=math_assistant,
    tool_name_override="math_teacher",
    tool_description_override="This is helpul math teacher ",
    on_handoff= service,
    input_type=MyInputData,
    input_filter=handoff_filters.remove_all_tools, # jo data hummy ksi or agent ko nhi dyna ya wo kamm krta ha 
    #is_enabled=tool_validate

)







# Create Triage agent with handoffs
triage_agent = Agent(
    name="Triage Agent",
    instructions="Tell me the Next.js routing.",
    handoffs=[next_js_assistant, python_assistant,math_teacher],# Only if supported by your Agent class
    model=MODEL ,
    tools=[get_weather],
    
)


#enable_verbose_stdout_logging()
