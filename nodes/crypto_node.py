from graph.state import FinPilotState
from tools.crypto_tool import get_crypto_price

def crypto_node(state:FinPilotState) -> FinPilotState:
    print("CRYPTO NODE EXECUTED")
    data=state['extracted_data']
    coin=data['coin']
    result=get_crypto_price.invoke({'coin':coin})
    state['result']=result

    return state