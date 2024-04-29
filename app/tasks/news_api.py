from newsapi import NewsApiClient
from app.config.settings import get_settings

settings = get_settings()


def fetch_news_api():
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(
        q="bitcoin",
        sources="bbc-news,the-verge",
        # category="business",
        language="en",
        country="us",
    )
    print("top_headlines: ", top_headlines)

    # /v2/everything
    all_articles = newsapi.get_everything(
        q="bitcoin",
        sources="bbc-news,the-verge",
        domains="bbc.co.uk,techcrunch.com",
        from_param="2017-12-01",
        to="2017-12-12",
        language="en",
        sort_by="relevancy",
        page=2,
    )
    print("all_articles: ", all_articles)

    # /v2/top-headlines/sources
    sources = newsapi.get_sources()
    print("sources: ", sources)
