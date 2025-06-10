from requests import get

from python_313.insides.colors import *
from python_313.insides.functions import _headers, write, addHTTP


def grabBanner(website):
    website = addHTTP(website)
    request = get(website, timeout=5, headers=_headers).headers.items()
    for headers in request:
        res = headers[0] + ": " + headers[1]
        write(var="#", color=c, data=res)
