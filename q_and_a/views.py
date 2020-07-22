from django.shortcuts import render

# Create your views here.
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

def index(request):
    return HttpResponsePermanentRedirect(reverse('homepage'))