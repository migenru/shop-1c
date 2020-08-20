from extuser.models import ExtUser
from sales_and_clients.cart import Cart
from .forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login

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




def cart(request):
    return {'cart': Cart(request)}

