from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')

def shop(request):
    context = {'games': [
        "Atomic Heart",
        "Cyberpunk 2077",
        "PayDay 2"
    ]}
    return render(request, 'shop.html', context=context)

def cart(request):
    return render(request, 'cart.html')



