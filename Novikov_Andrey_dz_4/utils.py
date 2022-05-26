from requests import get
import xml.etree.ElementTree as ETree
from decimal import Decimal
import datetime as dt


def currency_rates(currency):
    result = None
    date_obj = None
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = get(url)
    if response.status_code == 200:
        root_node = ETree.fromstring(response.text)
        date_str = root_node.get('Date')
        date_obj = dt.datetime.strptime(date_str, '%d.%m.%Y').date()
        for data in root_node:
            char_code = data.find('CharCode')
            if not(char_code is None) and char_code.text.lower() == currency.lower():
                value_str = data.find('Value').text.replace(',', '.')
                nominal_str = data.find('Nominal').text
                result = round(Decimal(value_str) / Decimal(nominal_str), 2)
    else:
        print('Ошибка при получении ответа с сервера.')
    response.close()

    return [result, date_obj]
