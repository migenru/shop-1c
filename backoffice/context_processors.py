from extuser.models import ExtUser
from catalog.models import Product


def fullname(request):
    '''
    Выводит в шаблоне Имя + Фамилия
    {{ fullname }}
    :param request:
    :return:
    '''
    username = request.user.username
    if username:
        user = ExtUser.objects.get(username=username)
        return {'fullname': user}
    else:
        return {'fullname': 'incognito'}


def incart(request):
    '''
    Выводит в шаблоне Имя + Фамилия
    {{ fullname }}
    :param request:
    :return:
    '''
    in_cart = request.COOKIES.get('cart')
    result = 0
    if in_cart:
        cart = in_cart[3:].split('_&_')
        productcarts = Product.objects.filter(pk__in=cart)
        for item in productcarts:
            result += item.price

    else:
        cart = []
    totalcart = len(cart)
    return {'incart': productcarts, 'totalcart': totalcart, 'cartresult': result}