# Программа для парсинга страницы ABBYY Lingvo

import requests
from bs4 import BeautifulSoup

URL = 'https://www.lingvolive.com/ru-ru/translate/ru-de/'
word = 'примечание'


# Функция для GET запроса страницы (аргумент URL)
def get_html(url):
    r = requests.get(url + word)
    return r


# Функция получения и обработки полученной HTML-страницы
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='_1mexQ Zf_4w _3bSyz')
    soup.h3.decompose()
    soup.h1.decompose()
    for tag in soup():
        del tag['data-reactid']
    return print(items)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        print('все норм')
        get_content(html.text)
    else:
        print('Error! Запрос не удался.')


parser()
