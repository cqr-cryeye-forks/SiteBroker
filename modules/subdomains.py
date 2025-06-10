import requests
from requests.exceptions import RequestException

from insides.colors import colors
from insides.functions import headers, removeHTTP, addHTTP
from insides.constants import subdomains


def findSubdomains(website: str) -> dict:
    result = {"subdomains": []}
    website = removeHTTP(website)
    for _sub in subdomains:
        if _sub:
            combo = f"{_sub}.{website}"
            full_url = addHTTP(combo)
            try:
                resp = requests.get(full_url, timeout=5, headers=headers).status_code
                if resp != 404:
                    result["subdomains"].append({
                        "url": full_url,
                        "status": resp
                    })
            except RequestException:
                pass
    return result