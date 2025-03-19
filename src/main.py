from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict
from src.services.bigquery_service import fetch_records

app = FastAPI()

class QueryInput(BaseModel):
    district: str
    mandal: str
    additional_var1_name: str
    additional_var1_value: Any

@app.post("/query")
def execute_query(query_input: QueryInput) -> Dict[str, Any]:
    records = fetch_records(
        district=query_input.district,
        mandal=query_input.mandal,
        additional_var1_name=query_input.additional_var1_name,
        additional_var1_value=query_input.additional_var1_value,
    )
    return {"records": records}