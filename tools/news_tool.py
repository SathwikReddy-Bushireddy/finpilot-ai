import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()
newsapi = NewsApiClient(
    api_key=os.getenv("NEWS_API_KEY")
)
def get_news(topic: str):
    try:
        articles = newsapi.get_everything(
            q=topic,
            language="en",
            sort_by="publishedAt",
            page_size=5
        )
        results = []
        for article in articles["articles"]:
            results.append({
                "title": article["title"],
                "source": article["source"]["name"],
                "url": article["url"]
            })
        return results
    except Exception as e:
        return {"error": str(e)}