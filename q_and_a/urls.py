from django.urls import path
from django.conf import settings

from q_and_a import views

urlpatterns = [
    path('', views.index, name='q-and-a'),
]
