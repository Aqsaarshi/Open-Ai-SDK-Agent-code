from pydantic import BaseModel

# Input datatype for multi-hotel detection
class MyDataType(BaseModel):
    is_query_about_known_hotel: bool
    hotel_name: str = None
    reason: str

# Output datatype for political content check
class OutputCheck(BaseModel):
    contains_political_content: bool
    reason: str
