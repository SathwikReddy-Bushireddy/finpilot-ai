from graph.state import FinPilotState
from utils.gemini import llm
import json

def router_node(state: FinPilotState):
    query = state["query"]
    history=state.get("history",[])
    prompt = f"""You are a financial AI assistant.
    Conversation History:{history}
    Current User Query:{query}
    Classify this query.
    Return ONLY JSON.
    Examples:
    {{"route":"stock"}}
    {{"route":"crypto"}}
    {{"route":"currency"}}
    {{"route":"news"}}
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