import json

import requests
from requests.exceptions import RequestException

from insides.colors import colors
from insides.functions import headers, write, Request, removeHTTP, addHTTP


def reverseViaHT(website: str) -> dict:
    result = {"domains": []}
    website = addHTTP(website)
    webs = removeHTTP(website)
    url = f"http://api.hackertarget.com/reverseiplookup/?q={webs}"
    try:
        response = Request(url, _timeout=5, _encode=True)
        if response and len(response) > 5:
            for domain in response.decode("utf-8").split("\n"):
                if domain:
                    result["domains"].append(domain)
    except RequestException as e:
        result["error"] = f"HackerTarget request failed: {str(e)}"
    return result

def reverseViaYGS(website: str) -> dict:
    result = {"ip": "", "domain": "", "total": 0, "domains": []}
    website = addHTTP(website)
    webs = removeHTTP(website)
    url = "https://domains.yougetsignal.com/domains.php"
    try:
        response = requests.post(url, headers=headers, data={'remoteAddress': webs}, timeout=5)
        data = response.json()
        if data['status'] != 'Fail':
            result["ip"] = data.get('remoteIpAddress', '')
            result["domain"] = data.get('remoteAddress', '')
            result["total"] = data.get('domainCount', 0)
            for domain in data.get('domainArray', []):
                result["domains"].append(domain[0])
    except (RequestException, json.JSONDecodeError) as e:
        result["error"] = f"YouGetSignal request failed: {str(e)}"
    return result
