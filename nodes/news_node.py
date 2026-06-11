from graph.state import FinPilotState
from tools.news_tool import get_news

def news_node(state: FinPilotState):
    topic = state["extracted_data"]["topic"]
    result = get_news(topic)
    state["result"] = result

    return state