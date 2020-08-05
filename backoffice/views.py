from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from extuser.models import ExtUser

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'backoffice/dashboard.html')
            else:
                return HttpResponse('Пользователь не найден')
        else:
            return HttpResponse('Неправильные логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'backoffice/login.html', {'form': form})


def main(request):
    return render(request, 'backoffice/dashboard.html')


def favorite_list(request):
    username = request.user.username
    user = ExtUser.objects.get(username=username)
    products = user.favorite_product.all()
    return render(request, 'backoffice/favorite.html', {'products':products})