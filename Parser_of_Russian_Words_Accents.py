import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import time

string: str = input('Enter the list of words: ')
division_symbol: str = input('Enter the symbol of division to form a list of words: ')

start = time()

list_of_words: list = string.split(division_symbol)
result_dict: dir = {

}

counter_of_errors: int = 0

for word in list_of_words:
    try:
        req = requests.get(f'https://где-ударение.рф/в-слове-{word}/')

    except:
        result_dict[word] = 'Error'

        counter_of_errors += 1

    else:
        try:
            bs = BeautifulSoup(req.text, 'html.parser')

            div_tag_text = bs.find('div', {'class': 'rule'}).text

            result = div_tag_text[div_tag_text.rfind('й') + 6:]

            result_dict[word] = result[:result.rfind('.')]


        except:
            result_dict[word] = 'Error'

            counter_of_errors += 1

pprint(result_dict)

print(f'\nNumber of words is {len(list_of_words)}')
print(f'Number of errors is {counter_of_errors}')
print(f'Errors are {(counter_of_errors/ len(list_of_words)) * 100}%')
print(f'Total time of program work: {round(time() - start, 3)} seconds')