import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data():
    # Faz a requisição à página da Steam
    url = 'https://store.steampowered.com/search/'
    params = {'supportedlang': 'pt-br',
            'category1': '998',
            'specials': '1',
            'ndl': '1',
            'start': '0',
            'excluded_content_types': '1'}

    # Faz a requisição à página da Steam
    page = requests.get(url, params=params)
    soup = BeautifulSoup(page.content, "html.parser")

    # Cria uma lista para armazenar os dados dos jogos
    games = []

    # Encontra todos os jogos na página
    soup = BeautifulSoup(page.content, "html.parser")

    # Encontra todos os jogos na página
    results = soup.find("div", {"class": "search_results"})
    game_containers = results.find_all("a", {"class": "search_result_row"})

    # Itera sobre cada jogo e coleta os dados desejados
    for game in game_containers:
        name = game.find("span", {"class": "title"}).get_text()
        
        if game.find("strike") is not None:
            original_price = game.find("strike").get_text()

        if game.find("div", {"class": "col search_price discounted responsive_secondrow"}) is not None:
            discount_price = game.find("div", {"class": "col search_price discounted responsive_secondrow"}).get_text().strip()

            discount_price = discount_price.split("R$")[1:][1] # Pega o preço com desconto

        url = game["href"]

        image_url = get_image(url)
        
        tag = get_tag(url)

        developer = get_developer(url)

        release_date = get_date(url)

        games.append([name, original_price, discount_price, image_url, url, tag, developer, release_date])

    # Cria um dataframe a partir da lista de jogos
    df = pd.DataFrame(games, columns=["Nome do jogo", "Preço original", "Preço com promoção", "URL da imagem", "URL do site original", "Primeiro marcador", "Desenvolvedora", "Data de lançamento"])

    return df
    
def get_image(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    image_container = soup.find("img", {"class": "game_header_image_full"})
    
    if image_container is None:
        return None

    return image_container["src"]
    
def get_tag(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")    

    tag_container = soup.find("div", {"class": "glance_tags popular_tags"})

    if tag_container is not None:
        tags = tag_container.find_all("a")
        if len(tags) > 0:
            first_tag = tags[0].get_text()
        else:
            first_tag = ""
    else:
        first_tag = ""

    return first_tag.strip()

def get_developer(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")    

    developer_container = soup.find("div", {"class": "dev_row"})

    if developer_container is not None:
        developer = developer_container.find("a").get_text()
    else:
        developer = None

    return developer

def get_date(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")    

    date_container = soup.find("div", {"class": "date"})

    if date_container is not None:
        date = date_container.get_text()
        date = date.split(",")[1].strip()
    else:
        date = None

    return date

if __name__ == '__main__':
    get_data()