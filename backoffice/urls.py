from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'backoffice'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('main/', views.main, name='main'),
    path('main/favorite', views.favorite_list, name='favorite'),
    path('logout/', LogoutView.as_view(next_page='catalog:index'), name='logout'),
]
