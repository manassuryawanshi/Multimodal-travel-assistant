from pydantic import BaseModel
from typing import Optional, List, Dict

class AgentState(BaseModel):
    city: str
    city_summary: Optional[str] = None

    # weather_forecast is now a DICT, not a list
    weather_forecast: Optional[Dict] = None

    image_urls: Optional[List[str]] = None
