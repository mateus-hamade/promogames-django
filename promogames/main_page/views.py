from django.shortcuts import render

from .models import main_page

# Create your views here.
def main(request):
    cards = main_page.objects.all()

    return render(request, 'main_page/main.html', {'cards': cards})