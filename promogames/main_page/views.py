from django.shortcuts import render
from .models import Game
from django.http import HttpResponse
import pandas as pd

from .scriptSteam import get_data_Steam
from .scriptNuuvem import get_data_Nuuvem
from .scriptGog import get_data_GOG

# Create your views here.
def main(request):
    search = request.GET.get('search')
    category = request.GET.get('category')
    developer = request.GET.get('developer')
    release = request.GET.get('release')

    cards = Game.objects.all()
    categories = Game.objects.values('tag').distinct()
    developers = Game.objects.values('developer').distinct()
    release_date = Game.objects.values('release_date').distinct()

    if search:
        cards = cards.filter(title__icontains=search)
    elif category:
        cards = cards.filter(tag__icontains=category)
    elif developer:
        cards = cards.filter(developer__icontains=developer)
    elif release:
        cards = cards.filter(release_date__icontains=release)

    # return render(request, 'main_page/main.html', {'cards': cards, 'categories': categories, 'developers': developers.order_by, 'release_date': release_date.order_by('-release_date')})

    # return render order by release date, category and developer
    return render(request, 'main_page/main.html', {'cards': cards, 'categories': categories.order_by('tag'), 'developers': developers.order_by('developer'), 'release_date': release_date.order_by('-release_date')})

def script(request): 
    if Game.objects.all().count() > 0:
        Game.objects.all().delete() 

    if True:
        df1 = get_data_Steam()

    for i in range(2):
        if i == 0 and True: 
            df2 = get_data_Nuuvem()
        if i == 1 and True:
            df2 = get_data_GOG()
            pass

        for index, row in df1.iterrows():
            for index2, row2 in df2.iterrows():
                if row['Nome do jogo'] == row2['Nome do jogo']:
                    if row['Preço com promoção'] > row2['Preço com promoção']:
                        df1.drop(index, inplace=True)
                    else:
                        df2.drop(index2, inplace=True)
        
        df1 = pd.concat([df1, df2], ignore_index=True)


    df1.sort_values(by=['Nome do jogo'], inplace=True)


    if df1 is not None:
        for index, row in df1.iterrows():
            game = Game(
                title = row['Nome do jogo'], 
                price = row['Preço original'],
                store = row['Loja'],
                discount_price = row['Preço com promoção'],
                image_url = row['URL da imagem'],
                link_url =row['URL do site original'],
                tag = row['Primeiro marcador'],
                developer = row['Desenvolvedora'],
                release_date = row['Data de lançamento'])
            game.save()
        
    return HttpResponse("Script executado com sucesso!")