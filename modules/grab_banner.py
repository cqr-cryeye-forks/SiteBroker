from requests import get, RequestException

from insides.functions import addHTTP


def grabBanner(website: str) -> dict:
    result = {"headers": {}}
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }

    try:
        website = addHTTP(website)
        response = get(website, timeout=5, headers=headers)
        for key, value in response.headers.items():
            result["headers"][key] = value
            # write(var="#", color=colors.c, data=f"{key}: {value}")
    except RequestException as e:
        result["error"] = f"Banner grabbing failed: {str(e)}"

    return result
