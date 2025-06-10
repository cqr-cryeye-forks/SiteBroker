import re
from typing import Optional, Union
import requests
from requests.exceptions import RequestException

from insides.colors import colors
from insides.constants import url_pattern, wrong_URL, empty_Website, headers


def webNotEmpty(website: str) -> str:
    if len(website) >= 1:
        return "valid"
    return "!valid"

def validWebsite(website: str) -> None:
    web = webNotEmpty(website)
    if web == "valid":
        if not re.match(url_pattern, website):
            raise ValueError(wrong_URL)
    else:
        raise ValueError(empty_Website)

def cleanURL(website: str) -> str:
    validWebsite(website)
    website = website.replace("http://", "")
    website = website.replace("http://www.", "")
    website = website.replace("https://", "")
    website = website.replace("https://www.", "")
    website = website.replace("www.", "")
    return website

def removeHTTP(website: str) -> str:
    return cleanURL(website)

def addHTTP(website: str) -> str:
    return f"http://{cleanURL(website)}"

def write(var: Optional[str], color: str, data: str) -> None:
    if var is None:
        print(f"{color}{data}")
    else:
        print(f"{colors.w}[{colors.g}{var}{colors.w}] {color}{data}")

def Request(website: str, _timeout: Optional[int] = None, _encode: Optional[bool] = None) -> Optional[Union[str, bytes]]:
    try:
        response = requests.get(website, headers=headers, timeout=_timeout)
        response.raise_for_status()
        if _encode is None:
            return response.content
        elif _encode:
            return response.text.encode('utf-8')
        return response.text
    except requests.exceptions.MissingSchema:
        return None
    except requests.exceptions.ContentDecodingError:
        return None
    except requests.exceptions.ConnectionError:
        return f"{colors.fg}{colors.sb}\n[$] Error: The website is either incorrect or down."
    except RequestException as e:
        return f"{colors.fc}{colors.sb}[$] Error: {colors.fg}{colors.sb}{str(e)}"