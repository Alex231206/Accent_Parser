import requests
from bs4 import BeautifulSoup
from pprint import pprint

string: str = input('Enter the list of words: ')
division_symbol: str = input('Enter the symbol of division to form a list of words: ')

list_of_words: list = string.split(division_symbol)
result_dict: dir = {

}

for word in list_of_words:
    try:
        req = requests.get(f'http://gramota.ru/slovari/dic?word={word}*&all=x&help=1')

    except:
        result_dict[word] = 'Error'

    else:
        try:
            bs = BeautifulSoup(req.text, 'html.parser')

            b_tag = bs.find('div', {'style': 'padding-left:50px'}).find('b')#.find('span', {'class': 'accent'})
            accent = b_tag.find('span', {'class': 'accent'}).text.upper()
            b_tag_text = str(b_tag)

            result = b_tag_text[b_tag.find('>') : b_tag_text.find('s') - 1] + accent + b_tag_text[b_tag_text.rfind('n') + 2 : b_tag_text.rfind('<')]

            result_dict[word] = result[3:]

        except:
            result_dict[word] = 'Error'

pprint(result_dict)