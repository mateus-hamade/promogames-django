import requests
import pandas as pd
from datetime import datetime

def get_data_GOG():
    gamelist = []
    for i in range(1,11):
        response = requests.get('https://embed.gog.com/games/ajax/filtered?mediaType=game&price=discounted&sort=popularity&page='+str(i))
        games = response.json()['products']

        if games == []:
            break

        for game in games:
            if game['price']['baseAmount'] == game['price']['finalAmount']:
                continue

            title_element = game['title']
            original_price = 'R$' + game['price']['baseAmount'].replace(".", ",")
            discount_price = game['price']['finalAmount'].replace(".", ",")
            url = 'https://www.gog.com' + game['url']
            image_url = game['image'] + '.png' 
            tag = game['genres'][0]
            developer = game['developer'].split(",")[0]

            if game['releaseDate'] == None:
                release_date = "Desconhecido"
            else:          
                release_date = datetime.fromtimestamp(game['releaseDate']).strftime('%Y')

            gamelist.append([title_element, original_price, discount_price, image_url, url, tag, developer, release_date, "GOG"])


    df = pd.DataFrame(gamelist, columns=["Nome do jogo", "Preço original", "Preço com promoção", "URL da imagem", "URL do site original", "Primeiro marcador", "Desenvolvedora", "Data de lançamento", "Loja"])
    
    return df


if __name__ == "__main__":
    get_data_GOG()