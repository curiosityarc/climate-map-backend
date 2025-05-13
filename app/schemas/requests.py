from pydantic import BaseModel

class TemperatureRequest(BaseModel):
    start_date: str
    end_date: str
