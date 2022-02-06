from ast import And
import json
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from basketapp.models import Basket

MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products:index', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'},
]

# Create your views here.
def main(request):
    products = Product.objects.all()[:4]

    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS,
        'products': products,
    })
    

def products(request, pk=None):
    categories = ProductCategory.objects.all()
    category = {'name': 'все'}
    products = Product.objects.all()[:4]

    if pk is not None and pk != 0:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = Product.objects.filter(category__pk=pk).order_by('price')

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu_links': MENU_LINKS,
        'categories': categories,
        'category': category,
        'products': products,
        'basket': basket,
    })
    

def category(request, pk=None):
    pass


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS,
    })
