from django.shortcuts import render

from .models import Game

from django.http import HttpResponse

from .script import get_data

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

    return render(request, 'main_page/main.html', {'cards': cards, 'categories': categories, 'developers': developers, 'release_date': release_date})

def script(request):
    df = get_data()
    # to save the data in the database
    for index, row in df.iterrows():
        game = Game(
            title = row['Nome do jogo'], 
            price = row['Preço original'],
            store = 'Steam',
            discount_price = row['Preço com promoção'],
            image_url = row['URL da imagem'],
            link_url =row['URL do site original'],
            tag = row['Primeiro marcador'],
            developer = row['Desenvolvedora'],
            release_date = row['Data de lançamento'])
        game.save()

    return HttpResponse("Script executado com sucesso!")