import re

import requests
from requests.exceptions import RequestException

from python_313.insides.colors import c, r
from python_313.insides.functions import _headers, write, removeHTTP


def browserspyRep(website: str) -> None:
    """Получает информацию о веб-сервере с browserspy.dk."""
    url = "http://browserspy.dk/webserver.php"
    _data = {'server': removeHTTP(website)}
    try:
        request = requests.post(url, headers=_headers, data=_data, timeout=5)
        request.raise_for_status()
        request = request.text
        _data = re.findall(r'<tr class="(.*)">\n<td class="property">(.*)</td>\n<td class="value">(.*)</td>\n</tr>',
                           request)
        for res in _data:
            result = res[1].capitalize() + ": " + res[2]
            write(var="#", color=c, data=result)
    except RequestException as e:
        write(var="!", color=r, data=f"BrowserSpy request failed: {str(e)}")
