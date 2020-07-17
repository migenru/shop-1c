from django.urls import path
from django.conf import settings

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog_list, name='catalog'),
]
