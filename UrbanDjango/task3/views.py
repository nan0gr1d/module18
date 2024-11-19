from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    context = {
        'item1': 'Galaxy Police 3',
        'item2': 'Arkanoid',
        'item3': 'Tetris',
    }
    return render(request, 'shop.html', context=context)

def cart(request):
    return render(request, 'cart.html')



