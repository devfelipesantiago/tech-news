from tech_news.database import search_news
import re
import datetime


# Requisito 6
def search_by_title(title):
    news = search_news({"title": re.compile(title, re.IGNORECASE)})
    list_news = []
    for new in news:
        list_news.append((new["title"], new["url"]))
    return list_news


# Requisito 7
def search_by_date(date):
    try:
        datetime.date.fromisoformat(date)
        news = search_news({"timestamp": re.compile(date)})
        list_news = []
        for new in news:
            list_news.append((new["title"], new["url"]))
        return list_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": re.compile(source, re.IGNORECASE)})
    list_news = []
    for new in news:
        list_news.append((new["title"], new["url"]))
    return list_news


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": re.compile(category, re.IGNORECASE)})
    list_news = []
    for new in news:
        list_news.append((new["title"], new["url"]))
    return list_news
