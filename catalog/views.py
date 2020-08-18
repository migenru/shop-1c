from django.shortcuts import render
from .models import Category, Product
from .other_func import currency_usd, currency_eur, weather_temp
from analytics.models import BlackIP
from .forms import SearchForm, FavoriteForm
from extuser.models import ExtUser
from django.shortcuts import get_object_or_404
from sales_and_clients.forms import CartAddProductForm
from django.http import HttpResponse
from django.views.generic.list import ListView


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


class CategoryListView(ListView):
    '''
    класс для вывода всех категорий
    '''
    model = Category
    template_name = 'catalog/catalog.html'
    context_object_name = 'catalogs'


def products_all(request):
    """Отображение всех товаров в магазине на одной странице"""
    products = Product.objects.all()
    return render(request, 'catalog/catalog_product_list.html', {'products': products})



class ProductListView(ListView):
    '''
    класс для вывод товара выбранной категории
    '''
    model = Product
    template_name = 'catalog/catalog_current_list.html'
    context_object_name = 'products'
    ordering = 'title'

    def get_queryset(self):
        cat = Category.objects.get(slug=self.kwargs['slug'])
        self.select_ordering = self.request.GET.get('ordering')
        if not self.select_ordering:
            self.select_ordering = 'title'
        return Product.objects.filter(categoty=cat).order_by(self.select_ordering)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['cat'] = Category.objects.get(slug=self.kwargs['slug'])
        return context





@block_detail
def product_card(request, slug):
    """Отображение карточки выбранного товара"""
    product = get_object_or_404(Product, slug=slug)
    favorite_product = Product.objects.get(slug=slug)
    if request.method == 'POST' and 'form' in request.POST:
        '''работа с формой добавления в избранное'''
        form = FavoriteForm(request.POST)
        if form.is_valid():
            user = ExtUser.objects.get(username=request.user.username)
            user.favorite_product.add(favorite_product)
            user.save()
            response = HttpResponse('Товар добавлен в избранное')
            return response
    else:
        form = FavoriteForm()

    if request.method == 'POST' and 'form_cart' in request.POST:
        '''работа с формой добавления в корзину'''
        form_cart = CartAddProductForm(request.POST)
        if form_cart.is_valid():
            if 'cart_id' not in request.COOKIES:
                cart_dict_id = ''
            else:
                cart_dict_id = request.COOKIES.get('cart_id')
            cart_dict_id += '_&_' + str(product.id)
            response = HttpResponse('Товар добавлен в корзину')
            response.set_cookie('cart_id', cart_dict_id)
            return response
    else:
        form_cart = CartAddProductForm()

    return render(request, 'catalog/catalog_product_detail.html',
                  {'product': product, 'form': form, 'form_cart': form_cart, })


def get_product(request):
    '''
    Функция отображения поиска
    :param request:
    :return:
    '''
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            get_title = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=get_title).exclude(quentity=0)
            return render(request, 'catalog/catalog_product_list.html', {'products': products})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'catalog/search.html', {'form': form})
