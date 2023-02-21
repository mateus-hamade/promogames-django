import requests
import pandas as pd
from datetime import datetime

def get_data_GOG():
    response = requests.get('https://embed.gog.com/games/ajax/filtered?mediaType=game&price=discounted&sort=popularity&page=1')
    games = response.json()['products']

    jogos = []

    for game in games:
        if game['price']['baseAmount'] == game['price']['finalAmount']:
            continue

        title_element = game['title']
        original_price = game['price']['baseAmount']
        discount_price = game['price']['finalAmount']
        url = 'https://www.gog.com' + game['url']
        image_url = game['image'] + '.png' 
        tag = game['genres'][0]
        developer = game['developer'].split(",")[0]

        if game['releaseDate'] == None:
            release_date = "Desconhecido"
        else:          
            release_date = datetime.fromtimestamp(game['releaseDate']).strftime('%Y')

        jogos.append([title_element, original_price, discount_price, image_url, url, tag, developer, release_date, "GOG"])


    df = pd.DataFrame(jogos, columns=["Nome do jogo", "Preço original", "Preço com promoção", "URL da imagem", "URL do site original", "Primeiro marcador", "Desenvolvedora", "Data de lançamento", "Loja"])
    

    return df


if __name__ == "__main__":
    get_data_GOG()