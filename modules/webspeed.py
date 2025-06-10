import socket
import time
from urllib.parse import urlparse

import requests
from requests.exceptions import RequestException

from insides.colors import colors
from insides.functions import headers, write, addHTTP


def websiteSpeed(website: str) -> dict:
    result = {}
    website = addHTTP(website)
    try:
        # DNS resolution time
        start = time.time()
        socket.gethostbyname(urlparse(website).netloc)
        result["dns_time"] = time.time() - start

        # Full load time
        start = time.time()
        requests.get(website, headers=headers, timeout=5).content
        load_time = time.time() - start
        result["load_time"] = load_time
        result["without_dns"] = load_time - result["dns_time"]
    except (socket.gaierror, RequestException) as e:
        result["error"] = f"Speed test failed: {str(e)}"
    return result
