import requests
from requests.exceptions import RequestException

from python_313.insides.colors import c, g, r
from python_313.insides.functions import _headers, Request, addHTTP, write


def findAdminPanel(website: str) -> None:
    """Ищет админ-панели на сайте."""
    website = addHTTP(website)
    try:
        panels = Request("https://raw.githubusercontent.com/Anon-Exploiter/Rough_Work/master/admin_panels",
                         _timeout=6, _encode=True)
        if panels:
            write(None, color=r, data="Failed to load admin panels list.")
            return
        panels = panels.split("\n")
        print("{}{:<92}| {:<50}".format(c, "URL", "STATUS"))
        for _panels in panels:
            if len(_panels) != 0:
                combo = website + "/" + _panels
                try:
                    resp = requests.get(combo, timeout=5, headers=_headers, allow_redirects=False).status_code
                    if resp == 200:
                        print("{}{:<92}| {:<50}".format(g, combo, resp))
                    elif resp == 301:
                        print("{}{:<92}| {:<50}".format(r, combo, "404"))
                    elif resp == 500 or resp == 502:
                        print("{}{:<92}| {:<50}".format(c, combo, "404"))
                    else:
                        print("{}{:<92}| {:<50}".format(r, combo, "404"))
                except RequestException:
                    print("{}{:<92}| {:<50}".format(r, combo, "404"))
    except Exception as e:
        write(None, color=r, data=f"Failed to process admin panels: {str(e)}")
