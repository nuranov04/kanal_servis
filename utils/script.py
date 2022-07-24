import requests
import xml.etree.ElementTree as ET

from datetime import date


def get_rate(currency: str) -> float:
    """
    func fot getting currency from site 'https://www.cbr.ru'
    :param currency: str
    :return: float
    """
    day = date.today().strftime('%d')         # |
    month = date.today().strftime('%m')       # |  getting date
    year = date.today().strftime('20%y')      # |

    url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}'  # creating url for request
    usd_rate = float(  # convert str to float
        ET.fromstring(requests.get(url).text).  # get request to url
        find(f'./Valute[CharCode="{currency}"]/Value').  # search currency in xml
        text.replace(',', '.'))  # replace ',' to '.'
    return usd_rate

