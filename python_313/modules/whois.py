from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from python_313.insides.colors import c, r
from python_313.insides.functions import write, Request, removeHTTP


def whoIS(website: str) -> None:
    """Performs WHOIS lookup for the website."""
    website = removeHTTP(website)
    url = f"https://www.whois.com/whois/{website}"
    try:
        request = Request(url, _timeout=5, _encode=None)
        if not request:
            write(var="!", color=r, data="Sorry, whois cannot be performed right now...!!! :[")
            return
        bs = BeautifulSoup(request, 'html.parser')
        results = bs.find_all('pre', {'class': 'df-raw'})
        if results:
            result = results[0].text
            print(f"\r{c}{result}")
        else:
            write(var="!", color=r, data="No WHOIS data found.")
    except RequestException as e:
        write(var="!", color=r, data=f"Sorry, whois cannot be performed right now: {str(e)}")
