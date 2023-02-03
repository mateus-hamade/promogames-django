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
    for data in get_data():
        try:
            aux = Game(title=data['title'], store='Steam', price=data['original_price'], image_url=data['image_link'], link_url=data['link_url'], discount_price=data['discount_price'])
            aux.save()
        except Exception:
            pass
    return HttpResponse("Script executado com sucesso!")