import requests
from requests.exceptions import RequestException

from insides.constants import headers
from insides.functions import Request, addHTTP


def findAdminPanel(website: str) -> dict:
    result = {"admin_panels": []}
    website = addHTTP(website)
    try:
        panels = Request("https://raw.githubusercontent.com/Anon-Exploiter/Rough_Work/master/admin_panels",
                         _timeout=6, _encode=True)
        if panels:
            for panel in panels.split("\n"):
                if panel:
                    url = f"{website}/{panel}"
                    try:
                        resp = requests.get(url, timeout=5, headers=headers, allow_redirects=False).status_code
                        result["admin_panels"].append({
                            "url": url,
                            "status": resp
                        })
                    except RequestException:
                        result["admin_panels"].append({
                            "url": url,
                            "status": "Request failed"
                        })
    except Exception as e:
        result["error"] = f"Admin panel search failed: {str(e)}"
    return result
