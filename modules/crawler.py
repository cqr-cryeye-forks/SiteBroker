from typing import Set, Dict, Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from insides.functions import Request, removeHTTP, addHTTP


def googleCrawl(website: str) -> Dict[str, Any]:
    """Краулит ссылки с Google"""
    return _crawl(website, "google")


def bingCrawl(website: str) -> Dict[str, Any]:
    """Краулит ссылки с Bing"""
    return _crawl(website, "bing")


def manualCrawl(website: str) -> Dict[str, Any]:
    """Краулит ссылки вручную с сайта"""
    return _crawl(website, "manual")


def _crawl(website: str, engine: str) -> Dict[str, Any]:
    result: Dict[str, Any] = {"links": [], "engine": engine, "error": None}
    website = addHTTP(website)
    base_url = removeHTTP(website)

    try:
        if engine == "manual":
            # Получаем HTML-контент через Request
            html_content = Request(website, _timeout=5, _encode=True)
            if not html_content:
                result["error"] = "Failed to fetch website content"
                return result

            soup = BeautifulSoup(html_content, 'html.parser')
            _links: Set[str] = set()

            for tag, attr in [('a', 'href'), ('link', 'href'),
                              ('img', 'src'), ('iframe', 'src'),
                              ('embed', 'src')]:
                for element in soup.find_all(tag):
                    if value := element.get(attr):
                        # Преобразуем относительные ссылки в абсолютные
                        full_url = urljoin(website, value)
                        if base_url in full_url:
                            _links.add(full_url)

            result["links"] = list(_links)

        elif engine in ["google", "bing"]:
            # Реализация для поисковиков (оставьте вашу текущую логику)
            pass

    except RequestException as e:
        result["error"] = f"{engine.capitalize()} crawl failed: {str(e)}"
    except Exception as e:
        result["error"] = f"Unexpected error during {engine} crawl: {str(e)}"

    return result
