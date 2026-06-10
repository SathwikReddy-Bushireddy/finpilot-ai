from typing import TypedDict

class FinPilotState(TypedDict):
    query: str
    route: str
    extracted_data: str
    result: str
    response: str
    