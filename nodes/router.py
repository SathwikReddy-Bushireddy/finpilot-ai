from graph.state import FinPilotState
from utils.gemini import llm
import json

def router_node(state: FinPilotState):
    query = state["query"]
    prompt = f"""Classify this query.
    Query:{query}
    Return ONLY JSON.
    Examples:
    {{"route":"currency"}}
    {{"route":"stock"}}
    {{"route":"crypto"}}
    """
    response = llm.invoke(prompt)
    content = response.content.strip()
    if content.startswith("```json"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()
    route = json.loads(content)
    state["route"] = route["route"]
    print("ROUTE: ",state['route'])

    return state