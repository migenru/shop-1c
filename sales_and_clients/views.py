from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product
from .forms import CartAddProductForm
from django.http import HttpResponse

# Create your views here.


def cart_add(request, slug):
    product = Product.objects.get(slug=slug)
    card_dict = str(product.id)
    response = render(request, 'sales_and_clients/cart_detail.html')
    response.set_cookie('cart', value=card_dict)
    return response


def cart_detail(request):
    return render(request, 'sales_and_clients/cart_detail.html', {})


