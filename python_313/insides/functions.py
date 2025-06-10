import re
from typing import Optional, Union
import requests
from requests.exceptions import RequestException

from python_313.insides.colors import fc, fg, sb, w, g
from python_313.insides.constants import url_pattern, wrong_URL, empty_Website, _headers

def webNotEmpty(website: str) -> str:
    """Проверяет, не пустой ли URL."""
    if len(website) >= 1:
        return "valid"
    return "!valid"

def validWebsite(website: str) -> None:
    """Валидирует URL, бросает исключение при ошибке."""
    web = webNotEmpty(website)
    if web == "valid":
        if not re.match(url_pattern, website):
            raise ValueError(wrong_URL)
    else:
        raise ValueError(empty_Website)

def cleanURL(website: str) -> str:
    """Удаляет схему и www из URL."""
    validWebsite(website)
    website = website.replace("http://", "")
    website = website.replace("http://www.", "")
    website = website.replace("https://", "")
    website = website.replace("https://www.", "")
    website = website.replace("www.", "")
    return website

def removeHTTP(website: str) -> str:
    """Удаляет HTTP/HTTPS из URL."""
    return cleanURL(website)

def addHTTP(website: str) -> str:
    """Добавляет http:// к URL."""
    return f"http://{cleanURL(website)}"

def write(var: Optional[str], color: str, data: str) -> None:
    """Печатает текст с цветовым форматированием."""
    if var is None:
        print(f"{color}{data}")
    else:
        print(f"{w}[{g}{var}{w}] {color}{data}")

def Request(website: str, _timeout: Optional[int] = None, _encode: Optional[bool] = None) -> Optional[Union[str, bytes]]:
    """Выполняет HTTP-запрос к сайту."""
    try:
        response = requests.get(website, headers=_headers, timeout=_timeout)
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
        return f"{fg}{sb}\n[$] Error: The website is either incorrect or down."
    except RequestException as e:
        return f"{fc}{sb}[$] Error: {fg}{sb}{str(e)}"