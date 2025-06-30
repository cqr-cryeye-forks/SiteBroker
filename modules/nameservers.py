from dns import resolver, exception
from insides.functions import removeHTTP


def nameServers(website: str) -> dict:
    """
    Возвращает словарь вида {"nameservers": [...]}.
    Если DNS-резолв завершился неудачно, добавляет ключ "error".
    """
    website = removeHTTP(website)
    result: dict[str, list[str] | str] = {"nameservers": []}

    def _query(domain: str) -> bool:
        """
        Пытается получить NS-для домена.
        Возвращает True, если записи найдены (даже одна), иначе False.
        """
        try:
            # raise_on_no_answer=False → вместо исключения вернётся пустой rrset
            ans = resolver.resolve(domain, "NS", raise_on_no_answer=False)
            if ans.rrset:
                result["nameservers"].extend(
                    str(r.target).rstrip(".") for r in ans
                )
                return True
        except (resolver.NXDOMAIN, resolver.Timeout) as e:
            result["error"] = f"DNS resolution failed: {e}"
        except exception.DNSException as e:
            result["error"] = f"DNS error: {e}"
        return False

    # 1. Пробуем полный домен demo.testfire.net
    if not _query(website):
        # 2. Если NS нет — пробуем зону второго уровня testfire.net
        zone_root = ".".join(website.split(".")[-2:])
        if zone_root != website:
            _query(zone_root)

    return result
