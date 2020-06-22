# Программа для парсинга страницы ABBYY Lingvo: https://github.com/malyshev-vladimir/parser_lingvo

import requests
from bs4 import BeautifulSoup

URL = 'https://www.lingvolive.com/ru-ru/translate/ru-de/'


# Функция для GET запроса страницы (аргумент URL)
def get_html(url, word):
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
    return items

def save_result(line):
    red_f = open('red_words.csv', 'a')
    red_f.write(line)
    red_f.close()

def parser(amount):
    with open('words.csv', 'r') as file:
        counter = 0
        for row in file:
            if counter < amount:
                red_row = row.split(',')
                # print(red_row) - проверка полученной строки
                counter += 1
                html = get_html(URL, red_row[1])
                if html.status_code == 200:
                    # print('все норм') - проверка правильности ответа
                    html_text = get_content(html.text)
                    red_row.append('"{}"'.format(html_text))
                    red_row[-1], red_row[1] = red_row[1], red_row[-1]
                    # print(red_row) - проверка полученного промежуточного результата
                    red_line = ','.join(red_row)
                    print(red_line)
                    save_result(red_line)
                else:
                    print('Error! Запрос не удался.')
            else:
                break
    # удалим использованные строчки
    with open('words.csv', 'r') as file:
        lines = file.readlines()
    lines = lines[amount:]
    with open('words.csv', 'w') as file:
        file.writelines(lines)



parser(50)
