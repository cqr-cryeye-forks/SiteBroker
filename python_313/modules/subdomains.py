import requests
from requests.exceptions import RequestException

from python_313.insides.colors import c, g, r
from python_313.insides.functions import headers, removeHTTP, addHTTP
from python_313.insides.constants import subdomains


def findSubdomains(website: str) -> None:
    """Scans for subdomains of the given website."""
    website = removeHTTP(website)
    print("{}{:<62}| {:<50}".format(c, "URL", "STATUS"))
    for _sub in subdomains:
        if len(_sub) != 0:
            combo = f"{_sub}.{website}"
            combo = addHTTP(combo)
            try:
                resp = requests.get(combo, timeout=5, headers=headers).status_code
                if resp != 404:
                    print("{}{:<62}| {:<50}".format(g, combo, resp))
                else:
                    print("{}{:<62}| {:<50}".format(r, combo, "404"))
            except RequestException:
                print("{}{:<62}| {:<50}".format(r, combo, "404"))
