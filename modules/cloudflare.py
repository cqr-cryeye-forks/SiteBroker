import re

import requests
from requests.exceptions import RequestException

from insides.constants import cloudflare_api_url, crimeflare_url, headers
from insides.functions import Request


def cloudflare(website: str) -> dict:
    result = {"protected": False, "real_ip": None}
    try:
        response = Request(f"{cloudflare_api_url}{website}", _timeout=3, _encode=True)
        if response and "cloudflare" in response.lower():
            result["protected"] = True
            # Attempt bypass
            post_data = {"cfS": website}
            bypass_resp = requests.post(crimeflare_url, headers=headers, data=post_data, timeout=5).text
            ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", bypass_resp)
            if ip_match:
                result["real_ip"] = ip_match.group(0)
    except RequestException:
        pass
    return result
