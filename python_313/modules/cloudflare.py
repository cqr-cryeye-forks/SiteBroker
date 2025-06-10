import re
from typing import Optional, Any

import requests
from requests.exceptions import RequestException

from python_313.insides.colors import c, g, y, b, fc, r
from python_313.insides.functions import write, Request
from python_313.insides.constants import cloudflare_api_url, crimeflare_url, headers


def cloudflare(website: str, _verbose: Optional[Any] = None) -> Optional[str]:
    """Проверяет наличие Cloudflare и пытается найти реальный IP."""
    if _verbose is not None:
        write(var="#", color=c, data=f"Checking For Cloudflare In {website}")
    combo = f"{cloudflare_api_url}{website}"
    try:
        request = Request(combo, _timeout=3, _encode=True)
        if request and "cloudflare" in str(request.lower()):
            if _verbose is not None:
                write(var="~", color=g, data="Cloudflare Found!\n")
                write(var="#", color=y, data="Trying To Bypass Cloudflare!\n")
            pos = {"cfS": website}
            res = requests.post(crimeflare_url, headers=headers, data=pos, timeout=5).text
            real_ip = None
            if re.findall(r"\d+\.\d+\.\d+\.\d+", res):
                reg = re.findall(r"\d+\.\d+\.\d+\.\d+", res)
                real_ip = reg[1] if len(reg) > 1 else reg[0]
            else:
                if _verbose is not None:
                    write(var="!", color=r, data="Sorry! Cloudflare Wasn't Bypassed :')")
            if real_ip:
                request = Request(f"http://{real_ip}", _timeout=3, _encode=True)
                if request and "cloudflare" not in str(request.lower()):
                    if _verbose is not None:
                        write(var="@", color=c, data="Cloudflare Bypassed!")
                        write(var="~", color=g, data=f"Real IP --> {fc}{real_ip}")
                    return str(real_ip)
                else:
                    if _verbose is not None:
                        write(var="!", color=r, data="Sorry! Cloudflare Wasn't Bypassed :')")
        else:
            if _verbose is not None:
                write(var="$", color=b, data=f"{website} Is not using Cloudflare!")
    except RequestException as e:
        if _verbose is not None:
            write(var="!", color=r, data=f"Cloudflare check failed: {str(e)}")
    return None