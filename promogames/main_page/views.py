from django.shortcuts import render

from .models import main_page

# Create your views here.
def main(request):
    search = request.GET.get('search')

    cards = main_page.objects.all()

    if search:
        cards = cards.filter(title__icontains=search)
        
    return render(request, 'main_page/main.html', {'cards': cards})