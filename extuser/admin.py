from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtUser

admin.site.register(ExtUser, UserAdmin)