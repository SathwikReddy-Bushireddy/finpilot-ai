from langgraph.graph import StateGraph,START,END
from graph.state import FinPilotState
from langgraph.checkpoint.memory import MemorySaver

from nodes.router import router_node
from nodes.crypto_node import crypto_node
from nodes.currency_node import currency_node
from nodes.response_node import response_node
from nodes.stock_node import stock_node
from nodes.extractor_node import extractor_node
from nodes.news_node import news_node

workflow=StateGraph(FinPilotState)

workflow.add_node('router',router_node)
workflow.add_node('extractor',extractor_node)
workflow.add_node('currency',currency_node)
workflow.add_node('stock',stock_node)
workflow.add_node('crypto',crypto_node)
workflow.add_node('response',response_node)
workflow.add_node('news',news_node)

workflow.add_edge(START,'router')
workflow.add_edge('router','extractor')
workflow.add_conditional_edges(
    "extractor",
    lambda state: state["route"],{
        "currency": "currency",
        "stock": "stock",
        "crypto": "crypto",
        "news": "news"
    }
)
workflow.add_edge('currency','response')
workflow.add_edge('stock','response')
workflow.add_edge('crypto','response')
workflow.add_edge('news','response')
workflow.add_edge('response',END)

checkpoint=MemorySaver()
graph=workflow.compile(checkpointer=checkpoint)