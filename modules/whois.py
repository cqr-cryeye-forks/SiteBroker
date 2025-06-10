from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from insides.functions import Request, removeHTTP


def whoIS(website: str) -> dict:
    result = {"data": None, "error": None}
    website = removeHTTP(website)
    url = f"https://www.whois.com/whois/{website}"
    try:
        request = Request(url, _timeout=5, _encode=None)
        if request:
            bs = BeautifulSoup(request, 'html.parser')
            results = bs.find_all('pre', {'class': 'df-raw'})
            if results:
                result["data"] = results[0].text
            else:
                result["error"] = "No WHOIS data found"
        else:
            result["error"] = "WHOIS lookup failed"
    except RequestException as e:
        result["error"] = f"WHOIS request failed: {str(e)}"
    return result
