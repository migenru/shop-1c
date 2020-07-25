from django.shortcuts import render
from .models import Category, Product
from .other_func import currency_usd, currency_eur, weather_temp
from analytics.models import BlackIP


def block_detail(func):
    """
    Декоратор который запрещает просмотр страниц, если пользователь
    находится в черном списке
    :param func:
    :return:
    """

    def wrapper(request, *args, **kwargs):
        ip_addr = request.META['REMOTE_ADDR']
        black_ip = BlackIP.objects.filter(black_address=ip_addr)
        if len(black_ip):
            return render(request, '404.html')
        else:
            return_value = func(request, *args, **kwargs)
            return return_value
    return wrapper


def index(request):
    """ОТображение главной страницы"""
    catalogs = Category.objects.all()
    catalogs_slider = Category.objects.all()[:3]
    context = {
        'temperature': weather_temp,
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


@block_detail
def product_card(request, slug):
    """Отображение карточки выбранного товара"""
    product = Product.objects.get(slug=slug)
    return render(request, 'catalog/catalog_product_detail.html', {'product': product})
