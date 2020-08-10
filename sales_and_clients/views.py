from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product
from .forms import CartAddProductForm
from django.http import HttpResponse

# Create your views here.


def cart_add(request, slug):
    product = Product.objects.get(slug=slug)
    value = request.COOKIES.get('cart')
    product_id = str(product.id)
    if value is None:
        value = dict()
    value[product_id] = {
        'title':'',
        'price':'',
        'slug':'',
    }
    value[product_id]['title'] = str(product.title)
    value[product_id]['price'] = str(product.price)
    value[product_id]['slug'] = str(product.slug)
    context = {
        'value': value,
    }
    response = render(request, 'sales_and_clients/cart_detail.html', context)
    response.set_cookie('cart', value)
    return response


def cart_detail(request):
    value = request.COOKIES.get('cart')
    context = {
        'value': value,
    }
    return render(request, 'sales_and_clients/cart_detail.html', context)


