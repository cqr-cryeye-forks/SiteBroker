from requests import get

from python_313.insides.colors import c
from python_313.insides.functions import write, addHTTP


def grabBanner(website):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    website = addHTTP(website)
    request = get(website, timeout=5, headers=headers).headers.items()
    for headers in request:
        res = f"{headers[0]}: {headers[1]}"
        write(var="#", color=c, data=res)
