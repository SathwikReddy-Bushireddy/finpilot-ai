from graph.state import FinPilotState
from utils.gemini import llm

def response_node(state: FinPilotState):
    print("RESPONSE NODE EXECUTED")
    query = state["query"]
    result = state["result"]
    prompt = f"""You are FinPilot AI, a financial assistant.\
    User Query:{query}
    Tool Output:{result}
    Generate a professional and user-friendly response.
    IMPORTANT:
    - Use the tool output.
    - Do not say you cannot access real-time data.
    - Do not mention limitations.
    - Present the information clearly.
    """
    response = llm.invoke(prompt)
    state["response"] = response.content

    return state