# Requisito 1
import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from tech_news.database import create_news

STATUS_CODE = 200
TIMEOUT = 3
SLEEP_TIME = 1


def fetch(url):
    """responsável por fazer a requisição HTTP"""
    time.sleep(SLEEP_TIME)
    try:
        response = requests.get(url, timeout=TIMEOUT)
    except requests.Timeout:
        return None

    if response.status_code != STATUS_CODE:
        return None

    return response.text


# Requisito 2
def scrape_noticia(html_content):
    """A função deve receber como parâmetro o conteúdo HTML da página"""

    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.find("link", {"rel": "canonical"})["href"]

    title = soup.find(id="js-article-title").get_text()

    timestamp = soup.time["datetime"]

    writer = None
    if soup.find("div", {"class": "z--font-bold"}):
        writer = soup.find("div", {"class": "z--font-bold"}).get_text().strip()
    else:
        writer = soup.find(id="js-author-bar").p.get_text().strip()

    selector = Selector(text=html_content)
    shares_count = 0
    share_count = selector.css(".tec--toolbar__item::text").get()
    if share_count:
        shares_count = (
            selector.css(".tec--toolbar__item::text").get().split()[0]
        )

    comments_count = list(
        soup.find("button", {"id": "js-comments-btn"}).descendants
    )[3][1:3]

    summary = (
        soup.find("div", {"class": "tec--article__body"}).p.get_text().strip()
    )

    selector = Selector(text=html_content)
    sources = []
    for source in selector.css(".z--mb-16 div a::text").getall():
        sources.append(source.strip())

    categories = []
    for category in soup.find(id="js-categories").find_all("a"):
        categories.append(category.string.strip())

    scrape_noticia = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count),
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }

    return scrape_noticia


# Requisito 3
def scrape_novidades(html_content):
    """Esta função fará o scrape da página
    Novidades para obter as URLs das páginas de notícias."""
    soup = BeautifulSoup(html_content, "html.parser")
    new_urls = []
    for new in soup.find_all(class_="tec--list__item"):
        new_urls.append(new.find("a")["href"])
    return new_urls


# Requisito 4
def scrape_next_page_link(html_content):
    """A função deve fazer o scrape deste
    HTML para obter a URL da próxima página"""
    soup = BeautifulSoup(html_content, "html.parser")

    if soup.find(class_="tec--btn--lg"):
        return soup.find(class_="tec--btn--lg")["href"]
    return None


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    news_list = []
    url = "https://www.tecmundo.com.br/novidades"

    while len(news_list) < amount:
        get_tech_news = scrape_novidades(fetch(url))

        for link in get_tech_news:
            news_data = scrape_noticia(fetch(link))
            news_list.append(news_data)
            if len(news_list) == amount:
                break

        url = scrape_next_page_link(fetch(url))

    create_news(news_list)
    return news_list
