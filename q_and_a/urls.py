from django.urls import path
from django.conf import settings

from q_and_a import views

app_name = 'q_and_a'
urlpatterns = [
    path('', views.index, name='index'),
]
