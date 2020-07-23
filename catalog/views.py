from django.shortcuts import render
from .models import Category, Product
from .other_func import currency_usd, currency_eur, weather_temp


def index(request):
    """ОТображение главной страницы"""
    catalogs = Category.objects.all()
    catalogs_slider = Category.objects.all()[:3]
    context = {
        'temperature' : weather_temp,
        'catalogs': catalogs,
        'catalogs_slider': catalogs_slider,
        'usd': currency_usd,
        'eur': currency_eur
    }
    return render(request, 'index.html', context=context)


def catalog_list(request):
    """Отображение списка категорий"""
    catalogs = Category.objects.all()
    return render(request, 'catalog/catalog.html', {'catalogs': catalogs})


def products_all(request):
    """Отображение всех товаров в магазине на одной странице"""
    products = Product.objects.all()
    return render(request, 'catalog/catalog_product_list.html', {'products': products})


def category_select(request, slug):
    """Отображение товаров выбранной категории на одной странице"""
    cat = Category.objects.get(slug=slug)
    products = Product.objects.all().filter(categoty=cat)
    return render(request, 'catalog/catalog_current_list.html', {'products': products, 'cat': cat})


def product_card(request, slug):
    """Отображение карточки выбранного товара"""
    product = Product.objects.get(slug=slug)
    return render(request, 'catalog/catalog_product_detail.html', {'product': product})
