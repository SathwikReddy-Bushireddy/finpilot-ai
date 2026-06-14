from typing import TypedDict,List

class FinPilotState(TypedDict):
    query: str
    route: str
    extracted_data: str
    result: str
    response: str
    history: List[str]
    