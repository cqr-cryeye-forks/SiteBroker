import re

import requests
from requests.exceptions import RequestException

from insides.constants import browserspy_url
from insides.functions import headers, removeHTTP


def browserspyRep(website: str) -> dict:
    result = {"server_info": {}}
    url = browserspy_url
    try:
        response = requests.post(url, headers=headers, data={"server": removeHTTP(website)}, timeout=5)
        matches = re.findall(r'<tr class=".*?">\n<td class="property">(.*?)</td>\n<td class="value">(.*?)</td>',
                             response.text)
        for prop, value in matches:
            result["server_info"][prop] = value
    except RequestException as e:
        result["error"] = f"BrowserSpy request failed: {str(e)}"
    return result
