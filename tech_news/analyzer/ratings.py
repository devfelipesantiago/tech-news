from tech_news.database import find_news


def top_5_news():
    """Seu código deve vir aqui"""
    news = find_news()
    top_news = []
    for new in news:
        top_news.append(
            {
                "title": new.get("title"),
                "url": new.get("url"),
                "sum_pop": new.get("comments_count") + new.get("shares_count"),
            }
        )
    sorted(top_news, key=lambda i: i["sum_pop"], reverse=True)
    return [(new["title"], new["url"]) for new in top_news][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news = find_news()
    categories = []
    for new in news:
        for category in new.get("categories"):
            categories.append(category)
    # sorted(categories, key=lambda i: i)
    categories.sort()
    return categories[:5]
