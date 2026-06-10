from langchain_core.tools import tool
import requests
@tool
def get_crypto_price(coin: str):
    """Get the current price of a crypto currency b it's ticker symbol"""
    try:
        url = (
            f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr"
        )
        response = requests.get(url)
        data = response.json()
        price = data[coin]["inr"]
        return f"{coin.capitalize()} price = ₹{price}"

    except Exception as e:
        return f"Error: {str(e)}"