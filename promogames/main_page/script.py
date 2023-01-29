import bs4 as bs
import urllib.request
import xml.etree.ElementTree

import numpy as np
import pandas as pd

def get_data():
    # abrindo uma conexão
    my_url = urllib.request.urlopen('https://store.steampowered.com/search/?sort_by=_ASC&ignore_preferences=1&specials=1&hidef2p=1&supportedlang=portuguese%2Cbrazilian&category1=998&os=win').read()

    # transformando em um objeto BeautifulSoup
    soup = bs.BeautifulSoup(my_url, 'lxml')

    # recuperando os dados
    data = soup.find_all('div', {'class': 'responsive_search_name_combined'})

    # pegando o href de cada jogo
    tag = soup.find_all('a', {'class': 'search_result_row ds_collapse_flag'})
    link = [x['href'] for x in tag]

    # pegar imagem de cada link
    image = []
    for i in range(len(link)):
        url_image = urllib.request.urlopen(link[i]).read()

        soup_image = bs.BeautifulSoup(url_image, 'lxml')

        tag_image = soup_image.find_all('img', {'class': 'game_header_image_full'})

        image.append([x['src'] for x in tag_image])

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

        link_image = str(image[i])[1:-1].replace("'", "")

        link_url = link[i]

        complet_list.append({"title": title, "discount": discount, "original_price": original_price, "image_link": link_image, "link_url": link_url, "discount_price": discount_price})

    return complet_list

def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

if __name__ == '__main__':
    get_data()