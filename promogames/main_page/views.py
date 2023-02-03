from django.shortcuts import render

from .models import Game

from django.http import HttpResponse

from .script import get_data

# Create your views here.
def main(request):
    search = request.GET.get('search')

    cards = Game.objects.all()

    if search:
        cards = cards.filter(title__icontains=search)
        
    return render(request, 'main_page/main.html', {'cards': cards})

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
            link_url =row['URL do site original'])
        game.save()

    return HttpResponse("Script executado com sucesso!")