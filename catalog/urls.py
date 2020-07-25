from django.urls import path
from django.conf import settings

from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog_list, name='catalog'),
    path('catalog/all/', views.products_all, name='products_all'),
    path('catalog/<slug:slug>/', views.category_select, ),
    path('catalog/product/<slug:slug>/', views.product_card, ),
]
