from graph.state import FinPilotState
from tools.currency_tool import convert_currency

def currency_node(state:FinPilotState) -> FinPilotState:
    print("CURRENCY NODE EXECUTED")
    data=state['extracted_data']
    amount=data['amount']
    from_currency=data['from_currency']
    to_currency=data['to_currency']
    result=convert_currency.invoke({'amount':amount,'from_currency':from_currency,'to_currency':to_currency})
    state['result']=result

    return state