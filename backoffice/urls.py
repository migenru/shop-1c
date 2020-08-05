from django.urls import path
from django.conf import settings

from . import views

app_name = 'backoffice'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('main/', views.main, name='main'),
]
