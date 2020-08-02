from django.urls import path
from django.conf import settings

from article import views

app_name = 'article'
urlpatterns = [
    path('content/<slug:slug>/', views.index, name='page'),
    path('blog/page/<slug:slug>/', views.blog_detail),
    path('blog/', views.blog_list, name='blog'),
]
