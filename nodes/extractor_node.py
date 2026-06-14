import json
from graph.state import FinPilotState
from utils.gemini import llm
def extractor_node(state: FinPilotState):
    query = state["query"]
    route = state["route"]
    history=state.get("history",[])
    prompt = f"""
    You are an information extraction assistant.
    conversation_history:{history}
    User Query:{query}
    Route:{route}
    Return ONLY valid JSON.
    For currency:{{
    "amount": number,
    "from_currency": "USD",
    "to_currency": "INR"
    }}
    For stock:{{
    "symbol": "AAPL"
    }}
    For crypto:{{
    "coin": "bitcoin"
    }}
    For news:
    {{
    "topic":"Tesla"
    }}
    Do not explain anything.Extract required information.Only return JSON.
    """
    response = llm.invoke(prompt)
    content = response.content.strip()
    if content.startswith("```json"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()
    extracted_data = json.loads(content)
    state["extracted_data"] = extracted_data

    return state