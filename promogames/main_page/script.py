import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data():
    # Faz a requisição à página da Steam
    url = "https://store.steampowered.com/search/?supportedlang=portuguese&category1=998&specials=1&ndl=1"
    page = requests.get(url)
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

        games.append([name, original_price, discount_price, image_url, url])

    # Cria um dataframe a partir da lista de jogos
    df = pd.DataFrame(games, columns=["Nome do jogo", "Preço original", "Preço com promoção", "URL da imagem", "URL do site original"])

    return df
    
def get_image(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    image_container = soup.find("img", {"class": "game_header_image_full"})
    
    return image_container["src"]
    
if __name__ == '__main__':
    get_data()