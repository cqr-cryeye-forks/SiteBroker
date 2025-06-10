from dns.resolver import resolve, NXDOMAIN, Timeout

from insides.functions import removeHTTP


def nameServers(website: str) -> dict:
    result = {"nameservers": []}
    website = removeHTTP(website)
    try:
        res = resolve(website, 'NS')
        for ns in res:
            result["nameservers"].append(str(ns))
    except (Timeout, NXDOMAIN) as e:
        result["error"] = f"DNS resolution failed: {str(e)}"
    return result
