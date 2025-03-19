from pydantic import BaseModel

class QueryInput(BaseModel):
    district: str
    mandal: str
    additional_var1_name: str
    additional_var1_value: str