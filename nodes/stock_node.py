from graph.state import FinPilotState
from tools.stock_tool import get_stock_price

def stock_node(state:FinPilotState) -> FinPilotState:
    print("STOCK NODE EXECUTED")
    data=state['extracted_data']
    symbol=data['symbol']
    result=get_stock_price.invoke({'symbol':symbol})
    state['result']=result

    return state