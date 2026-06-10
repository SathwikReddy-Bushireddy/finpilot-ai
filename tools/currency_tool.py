from langchain_core.tools import tool
import requests
@tool
def convert_currency(amount: float,from_currency: str, to_currency: str):
    """Convert an amount from one currency to another using live exchange rates."""
    try:
        url = (
            f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency.upper()}&to={to_currency.upper()}"
        )
        response = requests.get(url)
        data = response.json()
        converted_amount = data["rates"][to_currency.upper()]
        return (
            f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}"
        )
    except Exception as e:
        return f"Error: {str(e)}"