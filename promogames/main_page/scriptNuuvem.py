import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import pandas as pd

def get_data_Nuuvem():
    url = 'https://www.nuuvem.com/br-en/catalog/platforms/pc/price/promo/sort/bestselling/sort-mode/desc'

    # Fazer a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)

    # Analisar o conteúdo HTML usando o BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos os elementos que contêm informações dos jogos em promoção
    promo_game = soup.find('div', class_='products-dock products-dock__cards products-dock__cards__grid-5')
    promo_game_elements = promo_game.find_all('div', class_='product-card--grid')
    # Criar uma lista para armazenar os dados dos jogos em promoção
    games = []

    # Para cada jogo em promoção, extrair o título, preço e desconto
    for game_element in promo_game_elements:
        title_element = game_element.find('h3', class_='product-title single-line-name')
        price_element_Int = game_element.find('span', class_='integer')
        price_element_Dec = game_element.find('span', class_='decimal')
        discount_element = game_element.find('span', class_='product-price--discount')

        if title_element and price_element_Int and price_element_Dec and  discount_element:
            name = title_element.text.strip()
            discount_price = price_element_Int.text.strip() + price_element_Dec.text.strip()



        url = game_element.find('a', class_='product-card--wrapper', href=True)['href']
        
        original_price = get_original_price(url)

        image_url = game_element.find('img', alt=True)['src']

        tag = get_tag(url)

        developer = get_developer(url)        

        release_date = get_date(url)

        games.append([name, original_price, discount_price, image_url, url, tag, developer, release_date, "Nuuvem"])

    df = pd.DataFrame(games, columns=["Nome do jogo", "Preço original", "Preço com promoção", "URL da imagem", "URL do site original", "Primeiro marcador", "Desenvolvedora", "Data de lançamento", "Loja"])

    return df



def get_tag(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")    

    tag = soup.find('a', class_='label').get_text()
    
    return tag


def get_developer(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")    

    developer_container = soup.find('ul', class_='product-widget--list')

    developer = developer_container.find_all('li')[1].get_text()

    developer = developer.replace('\n', '').strip().split(':')

    developer = developer[1].strip()
    
    return developer


def get_date(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")    

    date_container = soup.find('ul', class_='product-widget--list')

    date = date_container.find_all('li')[0].get_text() # Y / D / M
    date = date.split('Release Date:')[0].strip()
    date = date.replace('\n', '-').split('-')

    return date[1]


def get_original_price(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")    

    original_price = soup.find('span', class_='product-price--old').get_text()

    return original_price

   
if __name__ == '__main__':
    get_data_Nuuvem()