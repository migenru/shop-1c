from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser




class ExtUser(AbstractUser):
    USER_TYPE = [
        ('S', 'Сотрудник'),
        ('C', 'Клиент'),
    ]
    second_name = models.CharField(verbose_name='Отчество', max_length=200, blank=True)
    user_type = models.CharField(verbose_name='Тип пользователя', choices=USER_TYPE, max_length=1, default='C')
    phone = models.CharField(verbose_name='Телефон', max_length=15, unique=True, blank=True)
    avatar = models.ImageField(verbose_name='Фото профиля', upload_to='user', blank=True)