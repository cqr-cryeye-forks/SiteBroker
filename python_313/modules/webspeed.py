import socket
import time
from urllib.parse import urlparse

import requests
from requests.exceptions import RequestException

from python_313.insides.colors import g, c
from python_313.insides.functions import headers, write, addHTTP


def websiteSpeed(website: str) -> None:
    """Measures DNS resolution and page load time for a website."""
    website = addHTTP(website)
    urlinfo = urlparse(website)

    try:
        start = time.time()
        ip = socket.gethostbyname(urlinfo.netloc)
        dns_tm = time.time() - start
        _dns = "{:<10}:{:>40} seconds".format(" DNS", dns_tm)
        write(var="~", color=g, data=_dns)

        start = time.time()
        _data = requests.get(website, headers=headers, timeout=5).content
        load_tm = time.time() - start
        _load = "{:<10}:{:>40} seconds".format(" Load", load_tm)
        _wo = "{:<10}:{:>40} seconds".format(" W/O DNS", load_tm - dns_tm)

        write(var="#", color=c, data=_load)
        write(var="~", color=g, data=_wo)
    except (socket.gaierror, RequestException) as e:
        write(var="!", color=r, data=f"Website speed test failed: {str(e)}")
