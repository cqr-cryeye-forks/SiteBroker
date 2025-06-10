import json

import requests
from requests.exceptions import RequestException

from python_313.insides.colors import c, r, b
from python_313.insides.functions import _headers, write, Request, removeHTTP, addHTTP


def reverseViaHT(website: str) -> None:
    """Выполняет обратный поиск IP через api.hackertarget.com."""
    website = addHTTP(website)
    webs = removeHTTP(website)
    url = "http://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    try:
        request = Request(combo, _timeout=5, _encode=True)
        if request and len(request) != 5:
            list = request.strip("").split("\n")
            for _links in list:
                if len(_links) != 0:
                    write(var="#", color=c, data=_links)
        else:
            write(var="@", color=r,
                  data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")
    except RequestException as e:
        write(var="!", color=r, data=f"HackerTarget request failed: {str(e)}")


def reverseViaYGS(website: str) -> None:
    """Выполняет обратный поиск IP через domains.yougetsignal.com."""
    website = addHTTP(website)
    webs = removeHTTP(website)
    url = "https://domains.yougetsignal.com/domains.php"
    post = {
        'remoteAddress': webs,
        'key': ''
    }
    try:
        request = requests.post(url, headers=_headers, data=post, timeout=5)
        request.raise_for_status()
        grab = json.loads(request.text)
        Status = grab.get('status')
        IP = grab.get('remoteIpAddress', '')
        Domain = grab.get('remoteAddress', '')
        Total_Domains = grab.get('domainCount', '0')
        Array = grab.get('domainArray', [])
        if Status == 'Fail':
            write(var="#", color=r, data="Sorry! Reverse Ip Limit Reached.")
        else:
            write(var="$", color=c, data="IP: " + IP)
            write(var="$", color=c, data="Domain: " + Domain)
            write(var="$", color=c, data="Total Domains: " + Total_Domains + "\n")
        for x, _ in Array:
            write(var="#", color=b, data=x)
    except (RequestException, json.JSONDecodeError) as e:
        write(var="!", color=r, data=f"YouGetSignal request failed: {str(e)}")
