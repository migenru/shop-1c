from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserForm
from extuser.models import ExtUser
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import date



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
    return render(request, 'backoffice/favorite.html', {'products': products})


def profile_edit(request):
    """
    Изменение профиля
    - если пользователь добавил аватар - на фото добавляется водяной знак "DJANGO SHOP"
    - если пользователь ввел дату рождения младше 18 лет - срабатывает редирект с ошибкой
    - если пользователь меняет пароль и они не совпадают - срабатывает редирект с ошибкой
    :param request:
    :return:
    """
    username = request.user.username
    modeluser = ExtUser.objects.get(username=username)
    if request.method == 'POST':
        form = UserForm(request.POST, files=request.FILES, instance=modeluser)
        if form.is_valid():
            cd = form.cleaned_data
            if form.has_changed():
                modeluser = form.save(commit=False)
                error_msg = ''
                # проверка на изменение поля new_password1 и new_password2
                if 'new_password1' in form.changed_data:
                    if cd['new_password1']!=cd['new_password2']:
                        error_msg += '<li>Пароли не совпадают!!!</li>'
                    else:
                        modeluser.set_password(cd['new_password1'])
                        modeluser.save()
                # проверка на возраст
                if 'birthday' in form.changed_data:
                    now_date = date.today()
                    my_age = cd['birthday']
                    delta_date = now_date - my_age
                    age18 = 18 * 365
                    if delta_date.days < age18:
                        error_msg += '<li>Лицам младше 18 - запрещено!!!</li>'
                if error_msg:
                    return HttpResponse('<ol>' + error_msg + '</ol>')
                form.save()
                # добавление водяного знака
                if 'avatar' in form.changed_data:
                    path_avatar='media/'+str(modeluser.avatar)
                    photo = Image.open(path_avatar)
                    drawing = ImageDraw.Draw(photo)
                    color = (169, 169, 169)
                    font = ImageFont.truetype("media/fonts/philosopher.ttf", 40)
                    pos = (0, 0)
                    text='DJANGO SHOP'
                    drawing.text(pos, text, fill=color, font=font)
                    photo.save(path_avatar)



            return render(request, 'backoffice/dashboard.html')
        else:
            context = {
                'form': form,
                'modeluser': modeluser
            }
            return render(request, 'backoffice/profile_edit.html', context)
    else:
        form = UserForm(instance=modeluser)
        context = {
            'form': form,
        }
        return render(request, 'backoffice/profile_edit.html', context)
