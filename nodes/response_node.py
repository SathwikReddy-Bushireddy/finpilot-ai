from graph.state import FinPilotState
from utils.gemini import llm

def response_node(state: FinPilotState):
    print("RESPONSE NODE EXECUTED")
    query = state["query"]
    result = state["result"]
    history=state.get("history",[])
    prompt = f"""You are FinPilot AI, a financial assistant.
    Conversation History:{history}
    User Query:{query}
    Tool Output:{result}
    Generate a professional and user-friendly response.
    You are FinPilot AI.
    User Query:{query}
    Tool Output:{result}
    If the tool output contains news articles:
    - Summarize the top stories.
    - Mention the source.
    - Keep it concise.
    - Use bullet points.
    IMPORTANT:
    - Use the tool output.
    - Do not say you cannot access real-time data.
    - Do not mention limitations.
    - Present the information clearly.
    """
    response = llm.invoke(prompt)
    state["response"] = response.content
    history = state.get("history",[])
    history.append(f"User: {query}")
    history.append(f"Assistant: {response.content}")
    state["history"] = history
    
    return state