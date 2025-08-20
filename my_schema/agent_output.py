from pydantic import BaseModel
#from dataclasses import dataclass


class MyDataOutput(BaseModel):
      n1: int 
      n2:int
      response:str = "Thanks"


class MyToolSchema(BaseModel):
    value1: int
    value2: int



# @dataclass
# class MyData:
#     n1 : int
#     n2 : int
#     res: str = "Thanks"
   

