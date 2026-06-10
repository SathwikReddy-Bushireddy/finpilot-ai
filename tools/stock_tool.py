from langchain_core.tools import tool
import yfinance as yf
@tool
def get_stock_price(symbol: str):
    """Get the current stock price and daily trading information for a given stock symbol"""
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return {
            "Company": info.get("shortName"),
            "Current Price": info.get("currentPrice"),
            "Day High": info.get("dayHigh"),
            "Day Low": info.get("dayLow")
        }
    except Exception as e:
        return {"error": str(e)}