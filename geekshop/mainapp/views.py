import json
from django.shortcuts import render

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]

# Create your views here.
def main(request):
    return render(request, 'index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
    })
    

def products(request):
    controls = [
        {'image': "img/controll.jpg"},
        {'image': "img/controll1.jpg"},
        {'image': "img/controll2.jpg"},
    ]

    with open('./products.json', 'r', encoding='UTF-8') as file:
        products = json.load(file)

    return render(request, 'products.html', context={
        'title': 'Продукты',
        'cntrls': controls,
        'products': products,
        'menu_links': MENU_LINKS,
    })
    

def contact(request):
    return render(request, 'contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
