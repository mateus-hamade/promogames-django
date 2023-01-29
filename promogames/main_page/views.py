from django.shortcuts import render

from .models import main_page

from django.http import HttpResponse

from .script import get_data

# Create your views here.
def main(request):
    search = request.GET.get('search')

    cards = main_page.objects.all()

    if search:
        cards = cards.filter(title__icontains=search)
        
    return render(request, 'main_page/main.html', {'cards': cards})

def script(request):
    for data in get_data():
        try:
            aux = main_page(title=data['title'], store='Steam', price=data['original_price'], image_url='https://picsum.photos/200/150', link_url='http://google.com', discount_price=data['discount_price'])
            aux.save()
        except Exception:
            pass
    return HttpResponse("Script executado com sucesso!")