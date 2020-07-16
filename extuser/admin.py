from django.contrib import admin

# Register your models here.

from .models import ExtUser

admin.site.register(ExtUser)