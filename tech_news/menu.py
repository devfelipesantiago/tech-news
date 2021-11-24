# Requisito 12
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
    search_by_source,
)


def analyzer_menu():
    menu = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    )

    options = {
        "0": get_tech_news,
        "1": search_by_title,
        "2": search_by_date,
        "3": search_by_source,
        "4": search_by_category,
        "5": top_5_news(),
        "6": top_5_categories(),
    }

    if menu == "7":
        sys.stdout.write("Encerrando script\n")
    elif menu not in options.keys():
        sys.stderr.write("Opção inválida\n")
    elif menu in ["5", "6"]:
        return options[menu]
    else:
        return options[menu](input(""))
