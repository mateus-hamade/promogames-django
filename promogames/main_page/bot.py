import bs4 as bs
import urllib.request
import xml.etree.ElementTree

import numpy as np
import pandas as pd

def get_data():
    # abrindo uma conexão
    my_url = urllib.request.urlopen('https://store.steampowered.com/search/?supportedlang=portuguese%2Cbrazilian&os=win&specials=1&hidef2p=1&ndl=1').read()

    # transformando em um objeto BeautifulSoup
    soup = bs.BeautifulSoup(my_url, 'lxml')

    # recuperando os dados
    data = soup.find_all('div', {'class': 'responsive_search_name_combined'})

    # remove the tags from the data
    data = [remove_tags(str(x)) for x in data]

    # remove the \t and \n from the data
    data = [x.strip() for x in data]
    data = [x.split('\n') for x in data]

    complet_list = []

    for i in range(len(data)):
        #apagar posição
        if len(data[i]) < 15:
            continue

        title = data[i][0]
        date = data[i][4]
        discount = data[i][11]
        original_price = []
        discount_price = []

        block = 0
        
        for j in range(len(data[i][14])-1, -1, -1):
            if block == 0:
                if data[i][14][j] == 'R':
                    block = 1   
                discount_price.append(data[i][14][j])
            else:
                original_price.append(data[i][14][j])

        
        original_price = original_price[::-1]
        discount_price = discount_price[::-1]

        original_price = ''.join(original_price)
        discount_price = ''.join(discount_price)

        complet_list.append([title, date, discount, original_price, discount_price])
    
    # print(complet_list)

    return complet_list


def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

if __name__ == '__main__':
    get_data()