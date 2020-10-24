from django.urls import path
from . import views

app_name='telebot'

urlpatterns = [
    path('', views.webhook, name="bot_start" ),
]