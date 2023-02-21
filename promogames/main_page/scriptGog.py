# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

def get_data_GOG():
    games = []
    page = requests.get('https://www.gog.com/en/games/discounted')
    soup = BeautifulSoup(page.content, "html.parser")

    container = soup.find('div', class_='paginated-products-grid grid')
    games = container.find_all('product-tile', class_='ng-star-inserted')

    for game in games:
        title_element = game.find('div', class_='product-tile__title').get_text().strip()
        price_element = game.find('span', class_='final-value')
        game.find()
        print( title_element, price_element)
        exit(1)

        discount_element = game.find('span', class_='product-price--discount')



        tag = get_tag(url)

        developer = get_developer(url)        

        release_date = get_date(url)

        games.append([name, original_price, discount_price, image_url, url, tag, developer, release_date, "Nuuvem"])

    df = pd.DataFrame(games, columns=["Nome do jogo", "Preço original", "Preço com promoção", "URL da imagem", "URL do site original", "Primeiro marcador", "Desenvolvedora", "Data de lançamento", "Loja"])

    return df



get_data_GOG()