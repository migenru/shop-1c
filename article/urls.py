from django.urls import path
from django.conf import settings

from article import views

app_name = 'article'
urlpatterns = [
    path('<slug:slug>/', views.index, name='page'),
]
