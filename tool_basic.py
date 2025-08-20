# tool_basic.py
from agents import enable_verbose_stdout_logging, function_tool , FunctionTool , RunContextWrapper
from my_schema.agent_output import MyToolSchema
from validator.validate_tool import tool_validate
# @function_tool
# def get_weather(city: str) -> str:
#     """Returns weather information for a given city."""
#     return f"The current temperature in {city} is 35°C."

@function_tool
def get_multiply(n1 : int , n2: int) -> str:
    """Return the information for a given value"""
    print("tool-->call")
    return f"Your answer is {n1 * n2}"

@function_tool              
#@function_tool(name_override="plus_tool", description_override="plus tool function", is_enabled=tool_validate) issy hum validate lga sakhty ha 
def get_plus(value : int) -> int:
    """Return the information for a given value"""
    print("tool-->call")
    return f"Plus the both {value}  "

@function_tool
def get_subtract(value : int) -> int:
    """Return the information for a given value"""
    print("tool-->call")
    return f"Subtract the both {value} "


#enable_verbose_stdout_logging()


# **CUSTOM TOOL **

async def subtract_function(ctx: RunContextWrapper, arg):
    print("Subtract tool --> fire")
    obj = MyToolSchema.model_validate_json(arg)
    return f"Your answer is {obj.value1 - obj.value2}."

subtract = FunctionTool(
    name="Subtract",
    description="Subtract function",
    params_json_schema=MyToolSchema.model_json_schema(),
    on_invoke_tool=subtract_function,
    is_enabled=tool_validate
)

@function_tool
def get_weather(city: str) -> str:
    """Returns weather information for a given city."""
    print("weather tool --> Fire")
    return f"The current temperature in {city} is 35°C."