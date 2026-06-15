# from utils.gemini import llm
# from tools.crypto_tool import get_crypto_price
# from tools.currency_tool import convert_currency
# from tools.stock_tool import get_stock_price
# response = llm.invoke("tesla stock price")
# print(response[''])
# print(convert_currency.invoke("Convert 500 EUR to INR"))
# print(get_stock_price.invoke({'symbol':"TSLA"}))
# print(get_crypto_price.invoke({'coin':"bitcoin"}))

# from graph.workflow import graph
# result = graph.invoke({"query": "What is Bitcoin price?"})
# print(result['response'])

# test_extractor.py
# from nodes.extractor_node import extractor_node
# state = {
#     "query": "Convert 500 EUR to INR",
#     "route": "currency"
# }
# result = extractor_node(state)
# print(result["extracted_data"])

from tools.news_tool import get_news
print(get_news("tesla"))