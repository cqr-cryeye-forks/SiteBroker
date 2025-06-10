import requests
from requests import RequestException

from insides.functions import headers, Request, addHTTP


def findShells(website: str) -> dict:
    result = {"shells": []}
    website = addHTTP(website)
    try:
        shells_list = Request("https://raw.githubusercontent.com/Anon-Exploiter/Rough_Work/master/shells",
                              _timeout=6, _encode=True).split("\n")
        for shell in shells_list:
            if shell:
                url = f"{website}/{shell}"
                try:
                    resp = requests.get(url, timeout=5, headers=headers, allow_redirects=False).status_code
                    result["shells"].append({
                        "url": url,
                        "status": resp
                    })
                except RequestException:
                    result["shells"].append({
                        "url": url,
                        "status": "Request failed"
                    })
    except Exception as e:
        result["error"] = f"Shell search failed: {str(e)}"
    return result
