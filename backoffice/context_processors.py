from extuser.models import ExtUser
from catalog.models import Product
from collections import Counter


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
    in_cart = request.COOKIES.get('cart_id')
    result = 0
    if in_cart:
        listcart = in_cart[3:].split('_&_')
        counter = Counter(listcart)
        productcarts = Product.objects.filter(pk__in=counter.keys())
        for item in productcarts:
            result += item.price
        totalcart = len(productcarts)

    else:
        productcarts = ''
        result = 0
        totalcart = 0

    return {'incart': productcarts, 'totalcart': totalcart, 'cartresult': result, 'cartamount': counter.values(),}