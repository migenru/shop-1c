from extuser.models import ExtUser


def fullname(request):
    '''
    Выводит в шаблоне Имя + Фамилия
    {{ fullname }}
    :param request:
    :return:
    '''
    username = request.user.username
    user = ExtUser.objects.get(username=username)
    return {'fullname': user.get_full_name}