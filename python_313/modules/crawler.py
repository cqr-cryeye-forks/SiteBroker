import re
from typing import Set

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from python_313.insides.colors import c, g
from python_313.insides.functions import headers, write, Request, removeHTTP, addHTTP


def googleCrawl(website: str) -> None:
    """Краулит ссылки с Google для указанного сайта."""
    search = "site:" + str(removeHTTP(website))
    webs = removeHTTP(website)
    for loop in range(0, 10):
        url = "https://google.com/search?q=" + str(search) + "&ie=utf-8&oe=utf-8&aq=t&start=" + str(loop) + "0"
        try:
            request = requests.get(url, headers=headers, timeout=5)
            request.raise_for_status()
            content = request.text
            soup = BeautifulSoup(content, 'lxml')
            sub_links = soup.find_all('div', class_='r')
            for links in sub_links:
                links = links.a['href']
                if str(webs) in links:
                    write(var="~", color=c, data=links)
        except RequestException:
            continue


def bingCrawl(website: str) -> None:
    """Краулит ссылки с Bing для указанного сайта."""
    search = "site:" + str(removeHTTP(website))
    webs = removeHTTP(website)
    link: Set[str] = set()
    for loop in range(0, 50):
        url = "http://www.bing.com/search?q=" + str(search) + "&first=" + str(loop) + "0"
        try:
            request = requests.get(url, headers=headers, timeout=5)
            request.raise_for_status()
            content = request.text
            links = re.findall(r'<a\shref="(.*?)"\sh="(.*?)">', content)
            if len(links) > 5:
                link.add(links[5][0])
        except RequestException:
            pass
    for links in link:
        if str(webs) in links:
            write(var="~", color=g, data=links)


def manualCrawl(website: str) -> None:
    """Краулит ссылки на указанном сайте."""
    website = addHTTP(website)
    webs = removeHTTP(website)
    request = Request(website, _timeout=5, _encode=True)
    if request:
        soup = BeautifulSoup(request, 'lxml')
        _links: Set[str] = set()
        for tag, attr in [('a', 'href'), ('link', 'href'), ('img', 'src'),
                          ('iframe', 'src'), ('embed', 'src')]:
            for element in soup.find_all(tag):
                if value := element.get(attr):
                    _links.add(value)
        for __links in _links:
            if str(webs) in __links:
                write(var="~", color=c, data=__links)
