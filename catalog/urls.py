from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.CategoryListView.as_view(), name='catalog'),
    path('catalog/all/', views.products_all, name='products_all'),
    path('catalog/<slug:slug>/', views.ProductListView.as_view(), ),
    path('catalog/product/<slug:slug>/', views.product_card, name='product_detail' ),
    path('search/', views.get_product, name="search" ),
]
