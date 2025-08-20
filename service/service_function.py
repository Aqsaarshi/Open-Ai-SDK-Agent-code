from agents import RunContextWrapper
from my_schema.input_schema import MyInputData

async def service(ctx: RunContextWrapper , input_data:MyInputData):
    print(ctx.context)     
    print(input_data.reason)