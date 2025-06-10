import re
from typing import Optional, Any

import requests
from requests.exceptions import RequestException

from python_313.insides.colors import c, g, y, b, fc, r
from python_313.insides.functions import _headers, write, Request


def cloudflare(website: str, _verbose: Optional[Any] = None) -> Optional[str]:
    """Проверяет наличие Cloudflare и пытается найти реальный IP."""
    if _verbose is not None:
        write(var="#", color=c, data="Checking For Cloudflare In " + website)
    combo = ("http://api-docs2.hackertarget.com/httpheaders/?q=" + str(website))
    try:
        request = Request(combo, _timeout=3, _encode=True)
        if request and "cloudflare" in str(request.lower()):
            if _verbose is not None:
                write(var="~", color=g, data="Cloudflare Found!\n")
                write(var="#", color=y, data="Trying To Bypass Cloudflare!\n")
            req = "http://www.crimeflare.biz/cgi-bin/cfsearch.cgi"
            pos = {'cfS': website}
            res = requests.post(req, headers=_headers, data=pos, timeout=5).text
            real_ip = None
            if re.findall(r'\d+\.\d+\.\d+\.\d+', res):
                reg = re.findall(r'\d+\.\d+\.\d+\.\d+', res)
                real_ip = reg[1] if len(reg) > 1 else reg[0]
            else:
                if _verbose is not None:
                    write(var="!", color=r, data="Sorry! Cloudflare Wasn't Bypassed :')")
            if real_ip:
                request = Request("http://" + str(real_ip), _timeout=3, _encode=True)
                if request and not "cloudflare" in str(request.lower()):
                    if _verbose is not None:
                        write(var="@", color=c, data="Cloudflare Bypassed!")
                        write(var="~", color=g, data="Real IP --> " + f"{fc}{real_ip}")
                    return str(real_ip)
                else:
                    if _verbose is not None:
                        write(var="!", color=r, data="Sorry! Cloudflare Wasn't Bypassed :')")
        else:
            if _verbose is not None:
                write(var="$", color=b, data=website + " Is not using Cloudflare!")
    except RequestException as e:
        if _verbose is not None:
            write(var="!", color=r, data=f"Cloudflare check failed: {str(e)}")
    return None
