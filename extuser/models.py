from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser




class ExtUser(AbstractUser):
    USER_TYPE = [
        ('S', 'Сотрудник'),
        ('C', 'Клиент'),
    ]
    second_name = models.CharField('Отчество', max_length=200, blank=True)
    user_type = models.CharField('Тип пользователя', choices=USER_TYPE, max_length=1, default='C')
    phone = models.CharField('Телефон', max_length=15, unique=True, blank=True)
    avatar = models.ImageField('Фото профиля', upload_to='user', blank=True)