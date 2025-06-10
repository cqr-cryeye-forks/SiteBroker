from dns.resolver import resolve, NXDOMAIN, Timeout

from python_313.insides.colors import c, r
from python_313.insides.functions import write, removeHTTP


def nameServers(website: str) -> None:
    """Получает DNS-серверы для указанного домена."""
    website = removeHTTP(website)
    try:
        res = resolve(website, 'NS')
        for nameservers in res:
            write(var="#", color=c, data=str(nameservers))
    except (Timeout, NXDOMAIN) as e:
        write(var="!", color=r, data=f"DNS resolution failed: {str(e)}")