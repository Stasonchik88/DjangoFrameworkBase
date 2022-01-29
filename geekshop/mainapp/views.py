import json
from unicodedata import category
from django.shortcuts import render
from .models import ProductCategory, Product

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products:index', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]

# Create your views here.
def main(request):
    products = Product.objects.all()[:4]

    return render(request, 'index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'products': products,
    })
    

def products(request, pk=None):
    categories = ProductCategory.objects.all()

    controls = [
        {'image': "img/controll.jpg"},
        {'image': "img/controll1.jpg"},
        {'image': "img/controll2.jpg"},
    ]

    with open('./products.json', 'r', encoding='UTF-8') as file:
        products = json.load(file)

    # products = 

    return render(request, 'products.html', context={
        'title': 'Продукты',
        'cntrls': controls,
        'categories': categories,
        'products': products,
        'menu_links': MENU_LINKS,
    })
    

def contact(request):
    return render(request, 'contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
